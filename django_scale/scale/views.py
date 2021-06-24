from django.shortcuts import render, redirect  # 追加
from django.contrib.auth import authenticate, login  # 追加
from django.utils import timezone 
import io
import base64
from datetime import datetime, timedelta
import math
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from matplotlib.dates import date2num
from matplotlib import ticker
from .forms import CustomUserCreationForm, UserForm
from .models import WeightTable
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dateutil.relativedelta import relativedelta

"""  日本語が使用できるように  """
matplotlib.rc('font', family='IPAPGothic')
""" 画像サイズの調整 """
plt.rcParams['figure.figsize'] = (15 ,5)

@login_required
def index(request): 
  params = {}

  age    = calc_age(request.user.birth)
  height = request.user.height

  """
  # テスト用
  import random
  today        = datetime.today()
  one_year_ago = today - timedelta(365)
  weight = 70.0
  for i in range((today - one_year_ago).days + 1):
    date = today + timedelta(i)
    int_random = random.randint(int(weight), int(weight+5))
    
    weight = random.uniform(int_random, 75.0)


    WeightTable.objects.create(
      user   = request.user,
      age    = age,
      height = height,
      weight = weight,
      created_date = date,
      )
  """
  result = create_graph(request.user, 30)
  if result is False:
      messages.error(request, 'まだ体重が一度も計測されていません。')
  graph = get_image()
  params['graph'] = graph

  if request.method == 'POST':
    form = UserForm(request.POST)

    weight = float(request.POST['weight'])
    

    if form.is_valid():
      WeightTable.objects.create(
        user   = request.user,
        age    = age,
        height = height,
        weight = weight,
        )

      
      latest_date = WeightTable.objects.latest("-created_date")

      healthy_weight  = calc_healthy_weight(height, weight)



      params = {
          'height'         : height, 
          'weihgt'         : weight,
          'healthy_weight' : healthy_weight, 
          'graph'          : graph,
          'form'           : form,
      }

    
  else:
    params['form'] = UserForm()
    
  return render(request, 'scale/index.html', params) 
  

def signup(request): 
  if request.method == 'POST': 
    form = CustomUserCreationForm(request.POST) 
    if form.is_valid(): 
      form.save()
      new_user   = authenticate( 
        email    = form.cleaned_data['email'] , 
        password = form.cleaned_data['password1'] , 
      ) 
      if new_user is not None: 
        login(request, new_user) 
        return redirect('scale:index') 
  else: 
    form = CustomUserCreationForm() 
  return render(request, 'scale/signup.html', {'form': form}) 
  

def get_image():

 buffer = io.BytesIO()
 plt.savefig(buffer, format='png', bbox_inches='tight')
 image_png = buffer.getvalue()
 graph = base64.b64encode(image_png)
 graph = graph.decode('utf-8')
 buffer.close()
 return graph


def create_graph(user, period):
  result = False
  
  user_data        = WeightTable.objects.filter(user=user)
  if len(user_data) == 0:
    return result
  latest_data = user_data.order_by('-created_date').first().created_date
  month_data = user_data.filter(created_date__range=[latest_data - timedelta(days=period), latest_data])
  weight_list = []
  date_list   = []
  for data in month_data:
    date_list.append(data.created_date)
    weight_list.append(data.weight)
  

  _, ax = plt.subplots()
  ax.plot(date_list, weight_list, color="red", marker="o", linestyle="solid")
  ax.set_title("体重推移")
  ax.set_xlabel("日付")
  ax.set_ylabel("体重")
  

  """ x軸の範囲を指定 """
  xmin=date_list[0]
  xmax=date_list[-1]
  ax.set_xlim(xmin, xmax) 
  
  """ メモリ設定の指定 """
  xloc = mdates.DayLocator()
  xfmt = mdates.DateFormatter("%m/%d")
  ax.xaxis.set_major_locator(xloc)
  ax.xaxis.set_major_formatter(xfmt)
  
  """ ラベルの設定 """
  labels = ax.get_xticklabels()
  plt.setp(labels, rotation=45, fontsize=10);

def calc_age(birth):
  birth = birth.strftime('%Y%m%d')  
  today = int(datetime.today().strftime("%Y%m%d"))
  return math.floor((today - int(birth)) / 10000)

def calc_healthy_weight(height, weight):
  healthy_weight = (height * height) * 22
  healthy_weight = round(healthy_weight, 2)
  
  return healthy_weight

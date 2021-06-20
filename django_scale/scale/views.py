from django.shortcuts import render 
from .forms import UserForm


def index(request): 
  params = {
      'height': 0, 
      'weihgt': 0,
      'form': None}
  if request.method == 'POST':
    form = UserForm(request.POST)
    height = float(request.POST['height']) /100
    weight = float(request.POST['weight'])

    bmi = weight / (height * height)
    bmi = round(bmi, 2)
    
    healthy_weight = (height * height) * 22
    healthy_weight = round(healthy_weight, 2)

    params['bmi']             = bmi
    params['healthy_weight']  = healthy_weight
    params['form'] = form      
  else:
    params['form'] = UserForm()
  return render(request, 'scale/index.html', params) 
  

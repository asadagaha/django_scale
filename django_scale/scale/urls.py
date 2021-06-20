from django.urls import path 
from . import views 
 
app_name = 'scale' 
urlpatterns = [ 
  path('', views.index, name='index'), 

] 
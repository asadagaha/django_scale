from django.db import models
from django.contrib.auth import get_user_model 
from django.utils import timezone 
# Create your models here.
class WeightTable(models.Model): 
  user            = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) 
  created_date    = models.DateTimeField("測定日時", default=timezone.now) 
  age             = models.IntegerField( "年齢",     blank=False, )
  height          = models.FloatField(   "身長",     blank=False, )
  weight          = models.FloatField(   "体重",     blank=False, )

  def __str__(self): 
    return self.user.email

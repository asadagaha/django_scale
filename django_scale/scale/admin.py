from django.contrib import admin
from .models import WeightTable 
# Register your models here.
class WeightTableAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_date','age', 'height', 'weight') 
    
    
admin.site.register(WeightTable, WeightTableAdmin) 
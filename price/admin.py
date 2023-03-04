from django.contrib import admin
from .models import Price_Calculate
# Register your models here.
@admin.register(Price_Calculate)
class User_Models_admin(admin.ModelAdmin):
  list_filter = ('Distance_Base_Price','Distance_travel','Distance_Additional_Price','Time_in_hours')
  list_display = ('Distance_Base_Price','Distance_travel','Distance_Additional_Price','Time_in_hours','final_price')
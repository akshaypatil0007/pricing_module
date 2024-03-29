from django.contrib import admin
from .models import Price_Calculate,Trips
# To add the data inside the databases directly from the project add it first into the admin.py
@admin.register(Price_Calculate)
class User_Models_admin(admin.ModelAdmin):
  list_filter = ('user','Distance_Base_Price','Distance_travel','Distance_Additional_Price','Time_in_hours')
  list_display = ('user','Distance_Base_Price','Distance_travel','Distance_Additional_Price','Time_in_hours')


@admin.register(Trips)
class trip_admin(admin.ModelAdmin):
  list_filter = ['user']
  list_display = ('user','final_price')






"""for add the data go to the django administrator and then add the data into the fields of table.
  
list_filter - add the filter into the django administrator
list_display - show the data that we added into the django administrator"""
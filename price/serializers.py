"""TO work with the django models we are using here serializer which is of django rest_framework:
here we create a new python file name as serializers.py inside app:"""

from .models import Price_Calculate
from rest_framework import serializers

class userSerializer(serializers.ModelSerializer):
  class Meta:
    model = Price_Calculate
    fields = ['Distance_Base_Price','Distance_travel','Distance_Additional_Price','Time_in_hours','final_price']
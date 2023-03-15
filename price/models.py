from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Here we build the structure for creating the database inside sqlite db

class Price_Calculate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100, null=True)
    Distance_Base_Price = models.IntegerField()
    Distance_travel = models.IntegerField()
    Distance_Additional_Price = models.IntegerField()
    Time_in_hours = models.IntegerField()
    Displayfields = ['Distance_Base_Price','Distance_travel','Distance_Additional_Price','Time_in_hours']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        final_price = (self.Distance_Base_Price + (self.Distance_travel * self.Distance_Additional_Price)) * self.Time_in_hours
        Trips.objects.filter(id=self.user).update(final_price=final_price)

# here we are creating the trip having the final price after calculating it from Price_Calculate table where user of
# Price_Calculate is foreign key of Trip user field
class Trips(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Price_Calculate, on_delete=models.CASCADE,null=True,blank=True)
    final_price = models.IntegerField(null=True)
    Displayfields = ['user', 'final_price']

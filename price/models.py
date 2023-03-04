from django.db import models

# Create your models here.
class Price_Calculate(models.Model):
    id = models.AutoField(primary_key=True)
    Distance_Base_Price = models.IntegerField()
    Distance_travel = models.IntegerField()
    Distance_Additional_Price = models.IntegerField()
    Time_in_hours = models.IntegerField()
    Displayfields = ['Distance_Base_Price','Distance_travel','Distance_Additional_Price','Time_in_hours','final_price']

    @property
    def final_price(self):
        DBP = self.Distance_Base_Price
        D = self.Distance_travel
        DAP = self.Distance_Additional_Price
        TBP = self.Time_in_hours
        final_price = (DBP + (D*DAP))*TBP
        return final_price


    # def save(self, *args, **kwargs):
    #       self.final_price = self.get_price_calc
    #       super(Price_Calculate, self).save(*args, **kwargs)

from django.db import models

# Here we build the structure for creating the database inside sqlite db
class Price_Calculate(models.Model):
    id = models.AutoField(primary_key=True)
    Distance_Base_Price = models.IntegerField()
    Distance_travel = models.IntegerField()
    Distance_Additional_Price = models.IntegerField()
    Time_in_hours = models.IntegerField()
    Displayfields = ['Distance_Base_Price','Distance_travel','Distance_Additional_Price','Time_in_hours','final_price']


# this final help to save the data into the final_price
    @property
    def final_price(self):
        DBP = self.Distance_Base_Price
        D = self.Distance_travel
        DAP = self.Distance_Additional_Price
        TBP = self.Time_in_hours
        final_price = (DBP + (D*DAP))*TBP
        return final_price


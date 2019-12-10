from django.db import models

class Squirrel(models.Model):

    X = models.FloatField(default=3)
    Y = models.FloatField(default=3)
    Unique_Squirre_ID = models.CharField(max_length=30, primary_key=True)
    Hectare =  models.CharField(max_length = 3)
    Shift = models.CharField(max_length=3)
    date = models.IntegerField(default=0)
    Hectare_Squirrel_Number = IntegerField(default=0)
    Age = models.IntegerField(default=0)
    Primary_Fur_Color = models.CharField(max_length=20)
    Highlight_Fur_Color = models.CharField(max_length=20)
    Combination_of_Primary_and_Highlight_Color =  models.CharField(max_length=20)

# Create your models here.

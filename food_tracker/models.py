from django.db import models

# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    purchage_date = models.DateField()
    epriry_date = models.DateField()

    def _str_(self):
        return self.name




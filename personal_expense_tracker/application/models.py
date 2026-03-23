from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)# categorizes expense
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.description
    
class Income(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    income_source = models.CharField(max_length=255,)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.income_source
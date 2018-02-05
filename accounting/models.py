from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ModelForm
from django_pandas.managers import DataFrameManager




class Document(models.Model):
    description = models.CharField(max_length=255, blank=False)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description



class Balance_Sheet(models.Model):
    description = models.CharField(max_length=255, blank=False)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description


# Create your models here.

# class Accounting(models.Model):
#     company = models.CharField(max_length=200)
#     history = models.CharField(max_length=200)
#     date = models.DateTimeField()
#     debit = models.CharField(max_length=100)
#     credit = models.CharField(max_length=100)
#     amount = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
#     conta_devedora = models.CharField(max_length=200)
#     conta_credora = models.CharField(max_length=200)
    #objects = models.Manager()
    #pdobjects = DataFrameManager()  # Pandas-Enabled Manager



    # def __str__(self):
    #     return self.history

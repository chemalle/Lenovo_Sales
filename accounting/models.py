from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db import models
from django_pandas.managers import DataFrameManager
from django.forms import ModelForm
#from data_importer.model import Accounting


class Books(models.Model):
    Type = models.CharField(max_length=200, blank=True)
    memo = models.CharField(max_length=500, blank=True)
    date = models.DateField()
    num = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=300, blank=True)
    split = models.CharField(max_length=500, blank=True)
    debit = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2,blank=True)
    credit = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2,blank=True)
    classification = models.CharField(max_length=500, blank=True)
    amount = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    debit_account = models.CharField(max_length=200)
    credit_account = models.CharField(max_length=200)
    # objects = models.Manager()
    # pdobjects = DataFrameManager()  # Pandas-Enabled Manager
    class Meta:
        unique_together = ['memo','num','amount','classification']

    def __str__(self):
        return self.memo


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



class Accounting(models.Model):
    company = models.CharField(max_length=200)
    history = models.CharField(max_length=200)
    date = models.DateField()
    debit = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)
    amount = models.DecimalField(default=0.0, max_digits=20, decimal_places=2)
    conta_devedora = models.CharField(max_length=200)
    conta_credora = models.CharField(max_length=200)
    objects = models.Manager()
    pdobjects = DataFrameManager()  # Pandas-Enabled Manager



    def __str__(self):
        return self.history

class MyAccounting(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='documents/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='documents/%Y/%m/%d/')



class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)

class Input(models.Model):
    email = models.EmailField(blank=True)

class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'

# Create the form class.


# Creating a form to add an article.
# >>> form = ArticleForm()
#
# # Creating a form to change an existing article.
# >>> article = Article.objects.get(pk=1)
# >>> form = ArticleForm(instance=article)

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

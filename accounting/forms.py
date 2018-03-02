from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Document, Balance_Sheet, Accounting

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')


class Statements(forms.ModelForm):
    class Meta:
        model = Balance_Sheet
        fields = ('description', 'document')


class AccountingForm(ModelForm):
     class Meta:
         model = Accounting
         fields = ['company', 'history', 'date', 'debit','credit','amount','conta_devedora','conta_credora']


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    #attach = forms.Field(widget = forms.FileInput)
    #comments = forms.CharField(required=False, widget=forms.Textarea)

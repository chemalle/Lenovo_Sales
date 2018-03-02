from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import django_excel as excel
from .models import Accounting, InputForm
from django.shortcuts import render_to_response
from datetime import datetime
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
import pyexcel as pe
from django.http import HttpResponse
from django import forms
from django.db.models import Sum
import datetime
import numpy as np
from decimal import Decimal
import decimal, simplejson
import json
from django_pandas.io import read_frame

import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import table

import datetime as dt

from accounting.forms import DocumentForm, Statements, AccountingForm

import numpy as np
import openpyxl

from django.core.files.storage import default_storage

from django.core.files import File
from xlrd import open_workbook

from django.forms import ModelForm

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


def home(request):
    return render(request, 'accounting/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'accounting/acc_active_sent.html')
            #return HttpResponse('Please confirm your email address to complete the registration.')
            # return render(request, 'acc_active_sent.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'accounting/thankyou.html')
    else:
        return HttpResponse('Activation link is invalid!')

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class DecimalJSONEncoder(simplejson.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)



@login_required
def Statements_Upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            GL_B = pd.read_excel(request.FILES['document'],'GL')

            GL = GL_B.to_csv('documents/FILE.csv')
            fields = ['Unnamed: 1','Type','Date','Num','Name','Memo','Split','Debit','Credit']

            GL = pd.read_csv('documents/FILE.csv', usecols=fields)
            GL['Classification'] = GL['Unnamed: 1'].fillna(method='ffill')
            GL = GL.fillna(0)

            BRAZIL = []

# For each row in the column,
            for row in GL['Classification']:
            # if more than a value,
                if row == 'Santander':
                # Append a letter grade
                    BRAZIL.append('1.1.01.002.0001')
                elif row == 'Santander Investment Account':
            # Append a letter grad
                    BRAZIL.append('1.1.01.003.0002')
                elif row == 'Accounts Receivable':
                # Append a letter grad
                    BRAZIL.append('1.1.02.001.0001')
                elif row == 'Deposit - Other':
                # Append a letter grad
                    BRAZIL.append('2.1.01.001.0003')
                elif row == 'Inventory':
                # Append a letter grad
                    BRAZIL.append('1.1.03.001.0001')
                elif row == 'Prepaid Commission':
                # Append a letter grad
                    BRAZIL.append('1.1.04.001.0003')
                elif row == 'Prepaid Reseller Commission':
                # Append a letter grad
                    BRAZIL.append('1.1.04.001.0004')
                elif row == 'Fixed Assets-Accum Depreciation':
                # Append a letter grad
                    BRAZIL.append('1.2.03.005.0000')
                elif row == 'Accounts Payable':
                # Append a letter grad
                    BRAZIL.append('2.1.01.001.0001')
                elif row == 'Accrued of Expenses':
                # Append a letter grad
                    BRAZIL.append('2.1.01.002.0001')
                elif row == 'Prepaid Reseller Cards':
                # Append a letter grad
                    BRAZIL.append('2.1.01.001.0002')
                elif row == 'Rixty USA Offset Liability':
                # Append a letter grad
                    BRAZIL.append('2.1.01.001.0009')
                elif row == 'Rixty USA Plat Offset Liability':
                # Append a letter grad
                    BRAZIL.append('2.1.01.001.0011')
                elif row == 'Taxes to Be Paid':
                # Append a letter grad
                    BRAZIL.append('2.1.01.003.0009')
                elif row == 'User Deposit':
                # Append a letter grad
                    BRAZIL.append('2.1.01.001.0003')
                elif row == 'Loan from Rixty USA':
                # Append a letter grad
                    BRAZIL.append('2.2.01.001.0001')
                elif row == 'Revenue':
                # Append a letter grad
                    BRAZIL.append('3.1.01.001.0001')
                elif row == 'Surcharge Revenue':
                # Append a letter grad
                    BRAZIL.append('3.1.01.001.0002')
                elif row == 'Commission Expense':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0009')
                elif row == 'Cost of Good Sold':
                # Append a letter grad
                    BRAZIL.append('3.2.01.001.0001')
                elif row == 'Advertising and Promotion':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0015')
                elif row == 'Bank Service Charges':
                # Append a letter grad
                    BRAZIL.append('3.3.01.002.0004')
                elif row == 'Computer and Internet Expenses':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0006')
                elif row == 'Depreciation Expense':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0002')
                elif row == 'CSLL -Income tax expenses':
                # Append a letter grad
                    BRAZIL.append('6.1.10.001.0002')
                elif row == 'IOF-Income tax expenses':
                # Append a letter grad
                    BRAZIL.append('3.3.01.002.0003')
                elif row == 'IRPJ - Income tax expenses':
                # Append a letter grad
                    BRAZIL.append('6.1.10.001.0001')
                elif row == 'ISS -Income tax expenses':
                # Append a letter grad
                    BRAZIL.append('3.1.02.001.0005')
                elif row == 'PIS/COFFINS -Income tax expense':
                # Append a letter grad
                    BRAZIL.append('3.1.02.001.0006')
                elif row == 'Marketing':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0015')
                elif row == 'Bonus':
                # Append a letter grad
                    BRAZIL.append('3.2.01.002.0001')
                elif row == 'Food Voucher':
                # Append a letter grad
                    BRAZIL.append('3.2.02.001.0008')
                elif row == 'Payroll Expenses':
                # Append a letter grad
                    BRAZIL.append('3.2.01.002.0001')
                elif row == 'FGTS - Taxes on payroll':
                # Append a letter grad
                    BRAZIL.append('3.2.02.001.0007')
                elif row == 'INSS-Taxes on payroll':
                # Append a letter grad
                    BRAZIL.append('3.2.02.001.0006')
                elif row == 'IRRF':
                # Append a letter grad
                    BRAZIL.append('3.2.01.002.0001')
                elif row == 'Postage and Delivery':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0007')
                elif row == 'Processing Fee':
                # Append a letter grad
                    BRAZIL.append('3.2.01.003.0003')
                elif row == 'Professional Fees':
                # Append a letter grad
                    BRAZIL.append('3.2.01.003.0003')
                elif row == 'Rent Expense':
                # Append a letter grad
                    BRAZIL.append('3.2.01.003.0006')
                elif row == 'Rounding Differences':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0017')
                elif row == 'Telephone Expense':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0006')
                elif row == 'Unknown Expenses':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0017')
                elif row == 'Unrealized Exchange Gain / Loss':
                # Append a letter grad
                    BRAZIL.append('3.3.02.002.0001')
                elif row == 'Interest Income':
                # Append a letter grad
                    BRAZIL.append('3.3.01.001.0003')
                elif row == 'Payroll':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0010')
                elif row == 'Income Tax Expense':
                # Append a letter grad
                    BRAZIL.append('6.1.10.001.0001')
                elif row == 'Automobile Expense':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0017')
                elif row == 'Fixed Assets':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0017')
                elif row == 'Printing and Reproduction':
                # Append a letter grad
                    BRAZIL.append('3.2.02.002.0010')
                else:
                    BRAZIL.append('Others')

            BRAZIL = pd.DataFrame(BRAZIL)
            GL['BRAZIL'] = BRAZIL

            GL['Debit'] = pd.to_numeric(GL['Debit'])
            GL['Credit'] = pd.to_numeric(GL['Credit'])

            GL = GL[GL['Split']!='']


            GL['debit account'] = np.where(GL['Debit']>0, GL['BRAZIL'], '5.1.01.001.0003')
            GL['credit account'] = np.where(GL['Credit']>0, GL['BRAZIL'], '5.1.01.001.0003')

            GL['R$'] = np.where(GL['Debit']>0, GL['Debit'], GL['Credit'])


            Revenue = GL.loc[GL['Classification'].values=='Revenue']
            Revenue = Revenue['Credit'] - Revenue['Debit']
            Surcharge_Revenue = GL[GL['Classification']=='Surcharge Revenue']
            Surcharge_Revenue = Surcharge_Revenue['Credit'] - Surcharge_Revenue['Debit']
            SALES= '{:,.2f}'.format(Revenue.sum() + Surcharge_Revenue.sum())
            SALES2 = Revenue.sum() + Surcharge_Revenue.sum()
            INTEREST = GL.loc[GL['Classification'].values=='Interest Income']
            INTEREST = INTEREST['Credit'] - INTEREST['Debit']
            Interest_Income = '{:,.2f}'.format(INTEREST.sum())
            Interest_Income2 = INTEREST.sum()
            ISS = '{:,.2f}'.format((Revenue.sum() + Surcharge_Revenue.sum()) * 0.05)
            Income_Tax_15 = '{:,.2f}'.format((SALES2* 0.32 )  + Interest_Income2)
            Tax_15 = '{:,.2f}'.format(((SALES2* 0.32 )  + Interest_Income2) * 0.15)
            Tax_15_b = ((SALES2* 0.32 )  + Interest_Income2) * 0.15
            Additional = '{:,.2f}'.format(((SALES2* 0.32 ) - 20000) * 0.10)
            Additional2 = ((SALES2* 0.32 ) - 20000) * 0.10
            Income_Tax_Ttl = '{:,.2f}'.format(Tax_15_b + Additional2)
            Income_Tax_Ttl2 = Tax_15_b + Additional2
            CSLL = '{:,.2f}'.format(((SALES2* 0.32 )  + Interest_Income2) * 0.09)
            CSLL2 = ((SALES2* 0.32 )  + Interest_Income2) * 0.09
            TTL = '{:,.2f}'.format(Income_Tax_Ttl2 + CSLL2)

            return render(request, 'tax.htm',{'SALES':SALES, 'Interest_Income':Interest_Income, 'ISS': ISS, "Income_Tax_15":Income_Tax_15,"Tax_15":Tax_15,
                            'Additional':Additional, 'Income_Tax_Ttl':Income_Tax_Ttl,'CSLL':CSLL, 'TTL': TTL})
#            return excel.make_response(pe.get_sheet(file_name='teste.xlsx'), "csv",file_name='forecast_2018')

    else:
        form = Statements()
    return render(
        request,
        'statements.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })

def __str__(self):
   return 'statements:' + self.name





# @login_required
def handson_table_accounting(request):
    return excel.make_response_from_tables(
    [Accounting], 'handsontable.html')



# @login_required
# def import_Accounting(request):
#     # if request.method == "POST":
    #     form = UploadFileForm(request.POST,
    #                           request.FILES)
    #     def choice_func(row):
    #         q = Question.objects.filter(slug=row[0])[0]
    #         row[0] = q
    #         return row
    #     if form.is_valid():
    #         request.FILES['file'].save_book_to_database(
    #             models=[Accounting],
    #             initializers=[None, choice_func],
    #             mapdicts=[
    #                 ['company','history', 'date', 'debit','credit','amount','conta_devedora','conta_credora']]
    #         )
    #         return render(request, 'accounting/thankyou2.html')
    #     else:
    #         return HttpResponseBadRequest()
    # else:
    #     form = UploadFileForm()
    # return render(
    #     request,
    #     'upload_form.html',
    #         {
    #         'form': form,
    #         'title': 'Import excel data into database',
    #         'header': "Please upload your accounting Journal:"
    #     })


@login_required
def Statements_Upload_Accounting(request):
    #df = Accounting.objects.filter(date__year=2018)
    df = pd.DataFrame(list(Accounting.objects.filter(date__year=2017).values()))
    #qs = Accounting.objects.all()
    #df = read_frame(qs)
    table_2016_credito = pd.pivot_table(df, values='amount',columns=['conta_credora'], aggfunc=np.sum)
    table_2016_debito = pd.pivot_table(df, values='amount',columns=['conta_devedora'], aggfunc=np.sum)
    table_2016_debito = pd.concat([table_2016_debito,pd.DataFrame(columns=table_2016_credito.columns)])
    table_2016_credito = pd.concat([table_2016_credito,pd.DataFrame(columns=table_2016_debito.columns)])
    table_2016_credito = table_2016_credito.fillna(0)
    table_2016_debito = table_2016_debito.fillna(0)
    balance = table_2016_debito - table_2016_credito
    cash = balance['Banco Itau'][-1]
    faturamento = balance['Faturamento'][-1]
    taxes = balance['Others'][-1]
    qs = Accounting.pdobjects.all()
    #df2 = qs.to_dataframe()

    #response = df2.to_html('accounting/templates/accounting/edu.html')
    #response2 = balance.to_html('accounting/templates/accounting/balance.html')


    #image_data = open("accounting/templates/accounting/mytable.png", "rb").read()
    #return HttpResponse(image_data, content_type="image/png")
    #return render(request,'accounting/edu.html')
    #return render(request,'accounting/balance.html')

    #teste = df.between_time(dt(2018,1,1) ,dt(2018-1-31))
    #df2 = pd.DataFrame(list(Accounting.objects.all().values('history', 'date', 'amount')))
    #df3 = pd.DataFrame(list(Accounting.objects.aggregate(Sum('amount'))))
    #df4 = df['amount'].sum()
    return render_to_response('accounting/name.html', context={'faturamento':faturamento,'cash':cash, "taxes":taxes})

def download(request):
    context = {

        'submit_btn': "excel"
        }
    return render(request, 'download.html',context)

def excel_download(request):
    qs = Accounting.pdobjects.all()
    df2 = qs.to_dataframe()
    fsock = df2.to_excel('accounting/templates/accounting/razao.xlsx',engine='openpyxl', index=False)
    fsock = open('accounting/templates/accounting/razao.xlsx', 'rb')
    response = HttpResponse(fsock, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="report.xls"'
    return response


@login_required
def General_Ledger(request):

    qs = Accounting.pdobjects.all()
    df2 = qs.to_dataframe()
    return render_to_response('accounting/ledger.html',{'data':df2.to_html(index=False,columns=['date','history','conta_devedora','conta_credora','amount'])})


@login_required
def Balance_Sheet(request):
    df = pd.DataFrame(list(Accounting.pdobjects.all().values()))
    #df = pd.DataFrame(list(Accounting.objects.filter(date__year=2017).values()))
    table_credito = pd.pivot_table(df, values='amount',columns=['conta_credora'], aggfunc=np.sum)
    table_debito = pd.pivot_table(df, values='amount',columns=['conta_devedora'], aggfunc=np.sum)
    table_debito = pd.concat([table_debito,pd.DataFrame(columns=table_credito.columns)])
    table_credito = pd.concat([table_credito,pd.DataFrame(columns=table_debito.columns)])
    table_credito = table_credito.fillna(0)
    table_debito = table_debito.fillna(0)
    balance = table_debito - table_credito
    cash = balance['Banco Itau'][-1]
    clientes = balance['Clientes'][-1]
    total_assets = cash + clientes
    taxes = balance['Impostos a Recolher'][-1]
    pl = balance['PL'][-1]
    total_liabilities = taxes + pl
    period = '2017'
    current_ratio = "{0:.2f}%".format(total_assets / -taxes)
    working_capital = '{0:,}'.format(total_assets + taxes)
    return render_to_response('accounting/index.html', context={'period':period,'current_ratio':current_ratio,'working_capital':working_capital,'cash':cash,'clientes':clientes,'taxes':taxes,'pl':pl, 'total_assets':total_assets, 'total_liabilities':total_liabilities})




@login_required
def Income_Statement(request):

    df = pd.DataFrame(list(Accounting.objects.filter(date__year=2017).values()))
    table_2016_credito = pd.pivot_table(df, values='amount',columns=['conta_credora'], aggfunc=np.sum)
    table_2016_debito = pd.pivot_table(df, values='amount',columns=['conta_devedora'], aggfunc=np.sum)
    table_2016_debito = pd.concat([table_2016_debito,pd.DataFrame(columns=table_2016_credito.columns)])
    table_2016_credito = pd.concat([table_2016_credito,pd.DataFrame(columns=table_2016_debito.columns)])
    table_2016_credito = table_2016_credito.fillna(0)
    table_2016_debito = table_2016_debito.fillna(0)
    balance = table_2016_debito - table_2016_credito
    cash = balance['Banco Itau'][-1]
    faturamento = '{:,.2f}'.format(-balance['Faturamento'][-1])
    taxes = '{:,.2f}'.format(-balance['Impostos sobre as vendas'][-1])
    net_income = '{:,.2f}'.format((-balance['Faturamento'][-1]) + (-balance['Impostos sobre as vendas'][-1]))
    cogs = '{:,.2f}'.format(-balance['Honorários Profissionais'][-1])
    gross_profit = '{:,.2f}'.format((-balance['Faturamento'][-1]) + (-balance['Impostos sobre as vendas'][-1]) + (-balance['Honorários Profissionais'][-1]))
    general = '{:,.2f}'.format((-balance['Impostos e Taxas'][-1]) + (-balance['INSS'][-1]))
    operating = '{:,.2f}'.format(-balance['Others'][-1])
    finance = '{:,.2f}'.format(-balance['Despesas Bancarias'][-1])
    expenses = '{:,.2f}'.format((-balance['Impostos e Taxas'][-1]) + (-balance['INSS'][-1]) + (-balance['Others'][-1]) + (-balance['Despesas Bancarias'][-1]))
    net_expenses = '{:,.2f}'.format((-balance['Faturamento'][-1]) + (-balance['Impostos sobre as vendas'][-1]) + (-balance['Honorários Profissionais'][-1]) + (-balance['Impostos e Taxas'][-1]) + (-balance['INSS'][-1]) + (-balance['Others'][-1]) + (-balance['Despesas Bancarias'][-1]))
    return render_to_response('accounting/dre.html', context={'faturamento':faturamento, "taxes":taxes,"net_income":net_income,"cogs":cogs, "gross_profit":gross_profit, 'general':general, "operating":operating,"finance":finance, "expenses":expenses, "net_expenses": net_expenses })








@login_required
def teste(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        def choice_func(row):
            q = Question.objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid:
            request.FILES['file'].save_book_to_database(
                models=[Accounting],
                initializers=[None, choice_func],
                mapdicts=[
                    ['company','history', 'date', 'debit','credit','amount','conta_devedora','conta_credora']]
                )
            return render(request, 'accounting/thankyou2.html')
    else:
        form = UploadFileForm()
        return render(
                        request,
                    'upload_form.html',
                    {
                    'form': form,
                    'title': 'Import excel data into database',
                    'header': "Please upload your accounting Journal:"
                    })




#import pandas as pd
#from .models import Accounting
# @login_required
# from django.conf import settings
#
# database_name = settings.DATABASES['default']['NAME']
#
# database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
#     user=user,
#     password=password,
#     database_name=database_name,
# )
#
# engine = create_engine(database_url, echo=False)
# df.to_sql(model._meta.db_table, con=engine)
#
#
#         return render(request, 'accounting/thankyou.html')

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import AccountingForm

def upload_file(request):
    if request.method == 'POST':
        form = AccountingForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render_to_response('accounting/thankyou2.html')
            #return HttpResponseRedirect('home.html')
    else:
        form = AccountingForm()
    return render(request, 'upload_form.html', {'form': form})



#
#
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# #from .forms import UploadFileForm
# from .models import MyAccounting
# from django.core.files.storage import FileSystemStorage
#
# def upload_file(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         form = UploadFileForm(request.POST, request.FILES)
#         fs = FileSystemStorage()
#         if form.is_valid():
#             GL = pd.read_excel(myfile)
#             GL['valor'] = 1.99
#             excel = GL.to_excel('documents/fantastico.xlsx',index=False)
#             filename = fs.save(myfile.name,myfile)
#             #book = openpyxl.load_workbook('documents/gl2.xlsx')
#             filename.save_book_to_database(
#                 models=[Accounting],
#                 #initializers=[None, choice_func],
#                 mapdicts=[
#                     ['company','history', 'date', 'debit','credit','amount','conta_devedora','conta_credora']]
#                 )
#             return render(request, 'accounting/thankyou2.html')
#     else:
#         form = UploadFileForm()
#         return render(
#                         request,
#                     'upload_form.html',
#                     {
#                     'form': form,
#                     'title': 'Import excel data into database',
#                     'header': "Please upload your accounting Journal:"
#                     })
# from django.http import HttpResponseRedirect
# from django.shortcuts import render

# from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

# @login_required
# def upload_file(request):
#     if request.method == 'POST':
#         form = AccountingForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             #handle_uploaded_file(request.FILES['file'])
#         return HttpResponseRedirect('thankyou2.html')
#     else:
#         form = Accountingform()
#
#         # df.save_book_to_database(
#         # models=[Accounting],
#         # initializers=[None, choice_func],
#         # mapdicts=[
#         #     ['company','history', 'date', 'debit','credit','amount','conta_devedora','conta_credora']])
#     return render(request, 'upload_form.html', {'form': form})
#
#
# def handle_uploaded_file(f):
#     df= pd.read_excel(f, index=False)
#     return df




# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# #from .forms import UploadFileForm
#
# # Imaginary function to handle an uploaded file.
# #from somewhere import handle_uploaded_file

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         def choice_func(row):
#             q = Question.objects.filter(slug=row[0])[0]
#             row[0] = q
#             return row
#         if form.is_valid():
#             handle_upload_file(request.FILES['file']).save_book_to_database(
#                 models=[Accounting],
#                 initializers=[None, choice_func],
#                 mapdicts=[
#                     ['company','history', 'date', 'debit','credit','amount','conta_devedora','conta_credora']]
#                 )
#             return render(request, 'accounting/thankyou2.html')
#
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload_form.html', {'form': form})
#
#
#
# def handle_uploaded_file(f):
#     GL = pd.read_excel(f, index=False)
#     GL['valor'] = 1.99
#     return GL.to_excel('documents/gl2.xls',index=False)


from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import UploadFileForm
from .models import MyAccounting

def upload2_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        #GL = pd.read_excel('documents/gl.xlsx')
        #GL['valor'] = 1.99
            #excel = GL.to_excel('documents/fantastico.xlsx',index=False)
            #book = openpyxl.load_workbook('documents/gl2.xlsx')
        request.FILES['file'].save_book_to_database(
                models=[Accounting],
                #initializers=[None, choice_func],
                mapdicts=[
                    ['company','history', 'date', 'debit','credit','amount','conta_devedora','conta_credora']]
                )
        return render(request, 'accounting/thankyou2.html')
    else:
        form = UploadFileForm()
        return render(
                        request,
                    'upload_form.html',
                    {
                    'form': form,
                    'title': 'Import excel data into database',
                    'header': "Please upload your accounting Journal:"
                    })


from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
@login_required
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        #GL = pd.read_excel(request.FILES['myfile'])
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        GL = pd.read_excel(filename)
        excel = GL.to_excel('documents/joia.xlsx')
        uploaded_file_url = fs.url('documents/joia.xlsx')
        return render(request, 'accounting/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'accounting/simple_upload.html')





# import os
#
# from django.conf import settings
# from django.http import JsonResponse
# from django.views.decorators.http import require_POST
#
# @require_POST
# def file_upload(request):
#     save_path = os.path.join(settings.MEDIA_ROOT, 'documents', request.FILES['file'])
#     path = default_storage.save(save_path, request.FILES['file'])
#     document = Accounting.objects.create(document=path, upload_by=request.user)
#     return JsonResponse({'document': document.id})





# from django.shortcuts import render
# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# @login_required
# def simple_upload2(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         #GL = pd.read_excel(request.FILES['myfile'])
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         GL = pd.read_excel(filename)
#         excel = GL.to_excel('documents/joia.xlsx')
#         uploaded_file_url = fs.url('documents/joia.xlsx')
#         return render(request, 'accounting/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'accounting/simple_upload.html')
#     uploaded_file_url.save_book_to_database(
#     models=[Accounting],
#     #initializers=[None, choice_func],
#     mapdicts=[
#         ['company','history', 'date', 'debit','credit','amount','conta_devedora','conta_credora']]
#     )
#     return render(request, 'accounting/thankyou2.html')



# class DataImporterCreateView(UploadFileForm):
#     extra_context = {'title': 'Create Form Data Importer',
#                      'template_file': 'myfile.csv'}
#     importer = Accounting
#
from data_importer.importers import CSVImporter
# #from data_importer.model import Accounting
class MyCSVImporterModel(CSVImporter):
    fields = ['company','history', 'date', 'debit','credit','amount','conta_devedora','conta_credora']
    class Meta:
         delimiter = ","
         model = Accounting
#

from tablib import Dataset
from .resources import PersonResource

def upload3_file(request):
    if request.method == 'POST' and request.FILES['file']:
        #form = DataImporterForm()
        #if form.is_valid:
        dataset = Dataset()
        GL = pd.read_excel(request.FILES['file'])
        csv = GL.to_csv('documents/agora.csv',index=False)
        #my_csv_list = MyCSVImporterModel(source="documents/agora.csv")
        imported_data = dataset.load(csv.read())
        result = person_resource.import_data(dataset, dry_run=True)
        return render(request, 'accounting/thankyou2.html')
    else:
        form = UploadFileForm()
        return render(
                        request,
                    'upload_form.html',
                    {
                    'form': form,
                    'title': 'Import excel data into database',
                    'header': "Please upload your accounting Journal:"
                    })


import tablib
#from .resources import PersonResource
from import_export import resources
from .models import Accounting

def csv_upload(request):
    if request.method == 'POST':
        new_persons = request.FILES['myfile']
        accounting_resource = resources.modelresource_factory(model=Accounting)()
        dataset = tablib.Dataset(['', 'New book'], headers=['id','empresa','historico','date','debito','credito','valor','conta_devedora','conta_credora'])
        imported_data = dataset.load(new_persons.read())
        result = accounting_resource.import_data(imported_data, dry_run=True) # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'accounting/import.html')




from tablib import Dataset
from import_export import resources
from .models import Person
#import csv
def csv_upload_persons(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['tnt']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.imported_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.imported_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'accounting/import.html')




#import csv,sys,os
from .models import Accounting
from django.http import HttpResponseRedirect

@login_required
def csv_upload_russo(request):
    if request.method == 'POST' and request.FILES['tnt']:
        GL = pd.read_excel(request.FILES['tnt'])
#        GL['valor']= '7777.77'
#        GL['historico'] = 'puta que pariu, consegui! Caralho!'
        GL['date']= pd.to_datetime(GL['date'])
        GL['valor'] = pd.to_numeric(GL['valor'])
#        data = GL.to_csv('documents/mycsv.csv',index=False)
#        data = csv.reader(open('documents/mycsv.csv'),delimiter=',')


        for index,row in GL.iterrows():
            if row[0] != 'create_date':
                accounting = Accounting()
                accounting.company = row[0]
                accounting.history = row[1]
                accounting.date = row[2]
                accounting.debit = row[3]
                accounting.credit = row[4]
                accounting.amount = row[5]
                accounting.conta_devedora = row[6]
                accounting.conta_credora = row[7]
                accounting.save()


        return render_to_response('accounting/thankyou2.html')

    else:
        return render(request, 'accounting/import.html')


class JournalListView(ListView):
    model = Accounting

    def get_queryset(self, *args, **kwargs):
        qs = super(JournalListView, self ).get_queryset(**kwargs)
        return qs


class JournalUpdateView(UpdateView):
    model = Accounting
    template_name = 'upload_form.html'
    form_class = AccountingForm
    success_url = "/accounting/"
    submit_btn = "Update Product"

#with open('some/path/to/file.csv') as f:
#    reader = csv.reader(f, delimiter=',')
#    header = next(reader)
#    Foo.objects.bulk_create([Foo(first_name=row[0], last_name=row[1]) for row in reader])




from django.core.mail.message import EmailMessage
from .models import Books
from django.http import HttpResponseRedirect
import numpy as np
from django.conf import settings
from django.core.files.storage import FileSystemStorage
@login_required
def xlsx_upload_accounting(request):
    if request.method == 'POST' and request.FILES['tnt']:
        myfile = request.FILES['tnt']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        GL_B = pd.read_excel(filename,'GL')
        GL = GL_B.to_csv('documents/statements.csv')
        fields = ['Unnamed: 1','Type','Date','Num','Name','Memo','Split','Debit','Credit']
        GL = pd.read_csv('documents/statements.csv', usecols=fields)
        GL['Classification'] = GL['Unnamed: 1'].fillna(method='ffill')
        GL = GL.fillna("")
        filter_col = [col for col in GL.Classification.unique() if not col.startswith('Total')]

        BRAZIL = []

        # For each row in the column,
        for row in GL['Classification']:
            # if more than a value,
            if row == 'Santander':
                # Append a letter grade
                BRAZIL.append('1.1.01.002.0001')
            elif row == 'Santander Investment Account':
                # Append a letter grad
                BRAZIL.append('1.1.01.003.0002')
            elif row == 'Accounts Receivable':
                # Append a letter grad
                BRAZIL.append('1.1.02.001.0001')
            elif row == 'Deposit - Other':
                # Append a letter grad
                BRAZIL.append('2.1.01.001.0003')
            elif row == 'Inventory':
                # Append a letter grad
                BRAZIL.append('1.1.03.001.0001')
            elif row == 'Prepaid Commission':
                # Append a letter grad
                BRAZIL.append('1.1.04.001.0003')
            elif row == 'Prepaid Reseller Commission':
                # Append a letter grad
                BRAZIL.append('1.1.04.001.0004')
            elif row == 'Fixed Assets-Accum Depreciation':
                # Append a letter grad
                BRAZIL.append('1.2.03.005.0000')
            elif row == 'Accounts Payable':
                # Append a letter grad
                BRAZIL.append('2.1.01.001.0001')
            elif row == 'Accrued of Expenses':
                # Append a letter grad
                BRAZIL.append('2.1.01.002.0001')
            elif row == 'Prepaid Reseller Cards':
                # Append a letter grad
                BRAZIL.append('2.1.01.001.0002')
            elif row == 'Rixty USA Offset Liability':
                # Append a letter grad
                BRAZIL.append('2.1.01.001.0009')
            elif row == 'Rixty USA Plat Offset Liability':
                # Append a letter grad
                BRAZIL.append('2.1.01.001.0011')
            elif row == 'Taxes to Be Paid':
                # Append a letter grad
                BRAZIL.append('2.1.01.003.0009')
            elif row == 'User Deposit':
                # Append a letter grad
                BRAZIL.append('2.1.01.001.0003')
            elif row == 'Loan from Rixty USA':
                # Append a letter grad
                BRAZIL.append('2.2.01.001.0001')
            elif row == 'Revenue':
                # Append a letter grad
                BRAZIL.append('3.1.01.001.0001')
            elif row == 'Surcharge Revenue':
                # Append a letter grad
                BRAZIL.append('3.1.01.001.0002')
            elif row == 'Commission Expense':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0009')
            elif row == 'Cost of Good Sold':
                # Append a letter grad
                BRAZIL.append('3.2.01.001.0001')
            elif row == 'Advertising and Promotion':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0015')
            elif row == 'Bank Service Charges':
                # Append a letter grad
                BRAZIL.append('3.3.01.002.0004')
            elif row == 'Computer and Internet Expenses':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0006')
            elif row == 'Depreciation Expense':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0002')
            elif row == 'CSLL -Income tax expenses':
                # Append a letter grad
                BRAZIL.append('6.1.10.001.0002')
            elif row == 'IOF-Income tax expenses':
                # Append a letter grad
                BRAZIL.append('3.3.01.002.0003')
            elif row == 'IRPJ - Income tax expenses':
                # Append a letter grad
                BRAZIL.append('6.1.10.001.0001')
            elif row == 'ISS -Income tax expenses':
                # Append a letter grad
                BRAZIL.append('3.1.02.001.0005')
            elif row == 'PIS/COFFINS -Income tax expense':
                # Append a letter grad
                BRAZIL.append('3.1.02.001.0006')
            elif row == 'Marketing':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0015')
            elif row == 'Bonus':
                # Append a letter grad
                BRAZIL.append('3.2.01.002.0001')
            elif row == 'Food Voucher':
                # Append a letter grad
                BRAZIL.append('3.2.02.001.0008')
            elif row == 'Payroll Expenses':
                # Append a letter grad
                BRAZIL.append('3.2.01.002.0001')
            elif row == 'FGTS - Taxes on payroll':
                # Append a letter grad
                BRAZIL.append('3.2.02.001.0007')
            elif row == 'INSS-Taxes on payroll':
                # Append a letter grad
                BRAZIL.append('3.2.02.001.0006')
            elif row == 'IRRF':
                # Append a letter grad
                BRAZIL.append('3.2.01.002.0001')
            elif row == 'Postage and Delivery':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0007')
            elif row == 'Processing Fee':
                # Append a letter grad
                BRAZIL.append('3.2.01.003.0003')
            elif row == 'Professional Fees':
                # Append a letter grad
                BRAZIL.append('3.2.01.003.0003')
            elif row == 'Rent Expense':
                # Append a letter grad
                BRAZIL.append('3.2.01.003.0006')
            elif row == 'Rounding Differences':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0017')
            elif row == 'Telephone Expense':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0006')
            elif row == 'Unknown Expenses':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0017')
            elif row == 'Unrealized Exchange Gain / Loss':
                # Append a letter grad
                BRAZIL.append('3.3.02.002.0001')
            elif row == 'Interest Income':
                # Append a letter grad
                BRAZIL.append('3.3.01.001.0003')
            elif row == 'Payroll':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0010')
            elif row == 'Income Tax Expense':
                # Append a letter grad
                BRAZIL.append('6.1.10.001.0001')
            elif row == 'Automobile Expense':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0017')
            elif row == 'Fixed Assets':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0017')
            elif row == 'Printing and Reproduction':
                # Append a letter grad
                BRAZIL.append('3.2.02.002.0010')
            else:
                BRAZIL.append('Others')

        BRAZIL = pd.DataFrame(BRAZIL)

        GL['BRAZIL'] = BRAZIL

        GL['Debit'] = pd.to_numeric(GL['Debit'])
        GL['Credit'] = pd.to_numeric(GL['Credit'])

        GL = GL[GL['Split']!='']

        GL['debit account'] = np.where(GL['Debit']>0, GL['BRAZIL'], '5.1.01.001.0003')
        GL['credit account'] = np.where(GL['Credit']>0, GL['BRAZIL'], '5.1.01.001.0003')
        GL['R$'] = np.where(GL['Debit']>0, GL['Debit'], GL['Credit'])
        GL = GL[['Type','Memo','Date','Num','Name','Split','Debit','Credit','Classification','R$', 'debit account','credit account']]
        GL.columns = ['Type','memo','date','num','name','split','debit','credit','classification','amount','debit account','credit account' ]
        GL['amount'] = GL['amount'].fillna(0)
        GL['debit'] = GL['debit'].fillna(0)
        GL['credit'] = GL['credit'].fillna(0)
        GL['memo'] = np.where(GL['memo']== '' , GL['name'] +" " + GL['num'], GL['memo'])


        GL['date']= pd.to_datetime(GL['date'])
        GL['amount'] = pd.to_numeric(GL['amount'])
        GL['debit'] = pd.to_numeric(GL['debit'])
        GL['credit'] = pd.to_numeric(GL['credit'])
        excel = GL.to_excel('statement.xlsx')

        names = []

        for i in filter_col:
            i = GL.loc[GL['classification'].values==i]
            i = i['debit'] - i['credit']
            names.append(i.sum())


        dictionary = dict(zip(filter_col, names))
        Santander = '{:,.2f}'.format(dictionary['Marketing'])


        for index,row in GL.iterrows():
            if row[0] != 'create_date':
                books = Books()
                books.Type = row[0]
                books.memo = row[1]
                books.date = row[2]
                books.num = row[3]
                books.name = row[4]
                books.split = row[5]
                books.debit = row[6]
                books.credit = row[7]
                books.classification = row[8]
                books.amount = row[9]
                books.debit_account = row[10]
                books.credit_account = row[11]
                books.save()

        email = EmailMessage()
        email.subject = "New Balance Sheet"
        email.from_email = "ThatAwesomeStatement! <no-reply@thatawesomeshirt.com>"
        email.to = [ "chemalle@me.com", ]

        email.attach_file('statement.xlsx') # Attach a file directly

        email.send()

        return render_to_response('accounting/thankyou2.html')
        raise Http404()

    else:
        return render(request, 'accounting/import.html')


from django.contrib import messages


def foo(request):
    # Some view where you want to throw error
    messages.add_message(request, messages.ERROR, 'Something Not Wrong')
    raise Http404()


@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            df = pd.read_excel(request.FILES['document'])
            writer = pd.ExcelWriter('teste.xlsx')
            filehandle = df.to_excel(writer)
            writer.save()
            return excel.make_response(pe.get_sheet(file_name='teste.xlsx'), "csv",file_name='forecast_2018')

    else:
        form = DocumentForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Forecast Scenario Creator',
            'header': ('Please choose your excel file ' +
                       'from your forecast repository:')
        })

def __str__(self):
   return 'form_upload:' + self.name


@login_required
def excel_download(request):
    fsock = open('documents/Orçamento Carrefour Porto Alegre - Lote 1159 - 28022018 Orc.xlsx', 'rb')
    response = HttpResponse(fsock, content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="quote.xlsx"'
    return response



from django.core.mail.message import EmailMessage
#from django.contrib.auth.models import User


@login_required
def email(request):
    if request.method == 'POST':
            form = EmailPostForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                email = EmailMessage()
                email.subject = "Your invoice just arrived"
                #message = 'RECEBEU!!!! AI CARALHO!'
                #email.from_email = "econobilidade@yahoo.com"
                email.to = [cd['to']]
                #email.bcc = []

                email.attach_file("documents/invoice.pdf", "application/pdf") # Attach a file directly

                email.send()
                return render_to_response('accounting/thankyou2.html')

    else:
        form = EmailPostForm(request.POST)


    return render(request, 'accounting/share.html', context = {'form': form})

from django.shortcuts import render, get_object_or_404
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
#from django.db.models import Count
from django.core.mail.message import EmailMessage
# from taggit.models import Tag

# from .models import Post, Comment
from .forms import EmailPostForm

@login_required
def email2(request):
    # Retrieve post by id
    #post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            #post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = "Your invoice just arrived"
            message = 'RECEBEU!!!! AI CARALHO!'
            # attached= email.attach_file('documents/Orçamento Carrefour Porto Alegre - Lote 1159 - 28022018 Orc.xlsx') # Attach a file directly

            send_mail(subject, message, 'admin@myblog.com', [cd['to']])

            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'accounting/share.html', {
                                                    'form': form,
                                                    'sent': sent})




def document(request):
    return render(request, 'accounting/document.html')

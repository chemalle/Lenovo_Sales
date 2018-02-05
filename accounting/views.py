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
#from .models import Accounting
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

from accounting.forms import DocumentForm, Statements

import numpy as np


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

class UploadFileForm(forms.Form):
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



@login_required
def import_Accounting(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        def choice_func(row):
            q = Question.objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Accounting],
                initializers=[None, choice_func],
                mapdicts=[
                    ['company','history', 'date', 'debit','credit','amount','conta_devedora','conta_credora']]
            )
            return render(request, 'accounting/thankyou2.html')
        else:
            return HttpResponseBadRequest()
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

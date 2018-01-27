from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^accounting/', views.import_Accounting, name="accountant"),
    url(r'^handson_view_accounting/', views.handson_table_accounting, name="handson_view_accounting"),
    url(r'^Accounting_query/$', views.Statements_Upload_Accounting, name='statements_query'),
    url(r'^General_Ledger/$', views.General_Ledger, name='GL'),
    url(r'^modelos/$', views.download, name='modelo'),#esta é apenas a interface para o download
    url(r'^download/$', views.excel_download, name='excel'),# isto realiza o download
    url(r'^Demonstrativos/$', views.Balance_Sheet, name='BS'),
    url(r'^DRE/$', views.Income_Statement, name='IS'),
]

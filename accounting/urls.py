from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^Taxes/$', views.Statements_Upload, name='statements'),
     url(r'^2018/$', views.model_form_upload, name='forecast'),#algoritmo de conversao xls
     url(r'^download/$', views.excel_download, name='proposal'),# isto realiza o download
     url(r'^email/$', views.email, name='email'),# isto realiza o download
     url(r'^document/$', views.document, name='doc'),# isto realiza o download
]

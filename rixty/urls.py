"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/12
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static  import static
from django.conf import settings

from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('accounting.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""PersonalWebSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
app_name = 'BabiGame'

from django.conf.urls import url
from django.contrib import admin
from BabiGame import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.babi_index, name='babi_index'),
    url(r'^foster', views.babi_foster, name='babi_foster'),
    url(r'^initBabiInfo', views.initBabiInfo, name='initBabiInfo'),
    url(r'^updateBabiInfo', views.updateBabiInfo, name='updateBabiInfo'),
    url(r'^saveBabiInfo', views.saveBabiInfo, name='saveBabiInfo'),
    url(r'^saveCompanyInfo', views.saveCompanyInfo, name='saveCompanyInfo'),
    url(r'^evaluateBabiInfo', views.evaluateBabiInfo, name='evaluateBabiInfo'),
]

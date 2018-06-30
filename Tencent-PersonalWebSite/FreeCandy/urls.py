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
app_name = 'FreeCandy'

from django.conf.urls import url
from django.contrib import admin
from FreeCandy import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', views.fc_index, name='dm_index'),
	url(r'^publish/', views.fc_publish, name='fc_publish'),
	url(r'^publishFreeCandy/', views.fc_publishFreeCandy, name='fc_publishFreeCandy'),
	url(r'^freeCandyDetail/', views.fc_freeCandyDetail, name='fc_freeCandyDetail'),
	url(r'^validGuestInfo/', views.fc_validGuestInfo, name='fc_validGuestInfo'),
	url(r'^getFreeCandy/', views.fc_getFreeCandy, name='fc_getFreeCandy'),
	# url(r'^valid/', views.dm_valid, name='dm_valid'),
	# # url(r'^detail/', views.dm_detail, name='dm_detail'),
	# url(r'^getDetailInfo', views.dm_getDetailInfo, name='dm_getDetailInfo'),
	# url(r'^search/', views.dm_search, name='dm_search'),
]

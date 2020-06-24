"""boke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from anima.views import *
from index.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',add_Views),
    #path(r'massage/',see_Views),
    path(r'massage/',paging_Views),
    url(r'^user/(\d+)',user_Views,name='username'),
    url(r'^detail/(\d+)',detail_Views,name='detail'),
    url(r'^del/(\d+)',del_Views,name='del'),
    path('tj/',adds_Views),
    path('tc/',tc_Views),
    url(r'^dm/',dm_Views,name='anime'),
    path('register/',register_Views,name='reg'),
    path('login/',login_Views),
    path('upload/',upload_Views),
    path('love/',love_Views),
    url(r'^love/(\d+)',love_Views,name='love'),
    path('class/daily', class_daily_Views),
    url(r'^class/daily/',class_daily_Views),
    # url(r'^addlove/(\d+)',addlove_Views,name='addlove'),

]

urlpatterns +=[
    path('Check_users/',Check_users_Voews),
    path('Check_dm',Check_dm_Views),
    path('loginout/',loginout_Views),
    path('Collection/',Collection_Views),
    path('anime/',anime_Views),
    url(r'^addlove/$',addlove_Views),
    path('del_Collection/',del_Collection_Views),
    path('dm_sort/',dm_sort_Views),


]


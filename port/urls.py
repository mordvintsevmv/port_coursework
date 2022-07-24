"""port URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf.urls import url


import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('all_transport/', views.all_transport),
    path('port_search/', views.port_search),
    path('in_port/', views.in_port),
    path('out_port/', views.out_port),
    path('transport_search/', views.transport_search),
    path('edit/', views.edit),
    path('login/', views.login),
    path('logout/', views.logout),
    path('add_user/', views.add_user)
]


"""tt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from  df_user import  views
from  goods import  views as goods
urlpatterns = [
    path('admin/', admin.site.urls),

    #用户
    path('register/',views.register),
    path('login/',views.login),
    path('index/',views.index),
    path('cart/',views.cart),
    path('user_center_info/',views.user_center_info),
    path('register_handle/',views.register_handle),
    path('login_handle/',views.login_handle),
    path('user_center_order/',views.user_center_order),
    path('user_center_site/',views.user_center_site),
    path('place_order/',views.place_order),
    path('list/',views.list),





    path('detail/',goods.detail),
    path('tinymce/',include('tinymce.urls'))






]

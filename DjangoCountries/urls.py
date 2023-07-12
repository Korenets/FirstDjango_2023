"""
URL configuration for FirstDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from DjangoCountries.views import HomepageView, counties, converter, first_symb, lang, first_lang
urlpatterns = [
    path('',HomepageView),
    path('countries-list/', counties),
    path('countries-list/<str:country>/', converter),
    path('countries-list/a/<str:symbol>/', first_symb),
    path('lang/', lang),
    path('lang/<str:data>/', first_lang),
    ]


"""
URL configuration for sports_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from sports import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main'),  # Main Page
    path('kabbadi/', views.kabbadi_page, name='kabbadi'),
    path('cricket/', views.cricket_page, name='cricket'),
    path('basketball/', views.basketball_page, name='basketball'),
    path('volleyball/', views.volleyball_page, name='volleyball'),
    path('input-names/', views.input_names, name='input_names'),
]



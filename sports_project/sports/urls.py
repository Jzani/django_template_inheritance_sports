from django.urls import path
from . import views

urlpatterns = [
    path('cricket/', views.cricket, name='cricket'),
    path('basketball/', views.basketball, name='basketball'),
    path('volleyball/', views.volleyball, name='volleyball'),
    path('kabaddi/', views.kabaddi, name='kabaddi'),
]

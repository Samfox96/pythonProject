from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('about', views.new),
    path('customer', views.customer),
    path('future', views.future),
    path('weather', views.weather)
]
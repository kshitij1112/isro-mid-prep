from django.urls import path
from SuryaDut import views


urlpatterns = [
    path('', views.brightness, name='brightness'),
]
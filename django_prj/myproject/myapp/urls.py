from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index') # url assigned to homepage
    ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.zerotestpage, name = 'zero test page'), #test main page
]
from django.urls import path
from . import views

urlpatterns =[
    path('', views.index), # root url
    path('new', views.new)
]
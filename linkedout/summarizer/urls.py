from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [    
    path('', views.index, name='index'),
    path('summarize/', views.summarize_post, name='summarize_post'),
]

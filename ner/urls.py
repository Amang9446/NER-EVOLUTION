from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('model/', views.model, name='model'),
    path('analyze/', views.analyze_text, name='analyze_text'),
    path('api/', views.api, name='api'),
    path('pricing/', views.pricing, name='pricing'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
    path('header/', views.header, name='header'),
  
]

from django.urls import path
from . import views


urlpatterns=  [
    path('', views.home_page, name='home'),
    path('analysis/', views.analysis_check, name='analysis'),
    path('fibonacci/', views.fibonacci_sequence, name='fibonacci'),
    path('binary/', views.binary_page, name='binary')
]

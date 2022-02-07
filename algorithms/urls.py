from django.urls import path

from . import views

urlpatterns = [
    path('algo_types/', views.getAlgorithmTypes, name='Algorithm Types'),
    path('algo_types/<str:pk>/', views.getAlgorithmType, name='Algorithm Type'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bubble_sort', views.bubbleSort, name="bubble_sort"),
]
# task.urls.py

from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='list'),
    path('update/<str:pk>/', views.updatingInternalKey, name='update'),
    path('delete/<str:pk>/', views.deleteInternalKey, name='delete'),
]
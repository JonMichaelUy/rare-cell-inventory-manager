from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('units/', views.units_index, name='index'),
  path('units/<int:unit_id>/', views.units_detail, name='detail'),
]
from django.urls import path
from . import views

from .views import SearchResultsView

urlpatterns = [
  path('', views.home, name='home'),
  path('units/', views.units_index, name='index'),
  path('units/<int:unit_id>/', views.units_detail, name='detail'),
  path('units/add/', views.AddUnit.as_view(), name='add_unit'),
  path('units/<int:pk>/edit/', views.EditUnit.as_view(), name='edit_unit'),
  path('units/<int:pk>/delete/', views.DeleteUnit.as_view(), name='delete_unit'),
  path("search/", SearchResultsView.as_view(), name="search_results"),
  path('accounts/signup/', views.signup, name='signup'),
]
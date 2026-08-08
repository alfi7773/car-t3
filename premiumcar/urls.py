from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cars/<int:id>/', views.detail, name='detail'),
    path('cars/catalogue/', views.catalogue, name='catalogue')
]

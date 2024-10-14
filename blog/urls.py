from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('reviews/', views.reviews_page, name='reviews'), 
]

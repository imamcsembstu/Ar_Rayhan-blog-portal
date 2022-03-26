from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='Dashboard'),
    path('home/', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('article/', views.article, name='Article'),
    path('lecture/', views.lecture, name='Lecture'),
    path('books/', views.books, name='Books'),
    path('contact', views.contact, name='Contact'),
]
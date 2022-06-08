from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),

    path('',views.books,name='books'),
    path('book-add/', views.addBook,name='book-add'),
    path('book-update/<str:pk>/', views.updateBook, name='book-update'),
    path('book-delete/<str:pk>/', views.deleteBook, name='book-delete'),


]

from django.urls import path
from .views import book_list,create_book,book,update_book,delete_book

urlpatterns = [
    path("get-books",book_list),
    path("create-book",create_book),
    path("book/<str:pk>/",book),
    path("update-book/<str:pk>/",update_book),
    path("delete-book/<str:pk>/",delete_book),
]
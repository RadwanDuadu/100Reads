from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]
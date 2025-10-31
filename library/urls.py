from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
    path(
        'moderator/dashboard/',
        views.moderator_dashboard,
        name='moderator_dashboard'
        ),
    path(
        'moderator/review/<int:review_id>/approve/',
        views.approve_review,
        name='approve_review'
     ),
    path(
        'moderator/review/<int:review_id>/delete/',
        views.delete_review,
        name='delete_review'
        ),
]

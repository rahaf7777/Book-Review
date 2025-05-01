from django.urls import path
from .views import (
    RegisterView, ChangePasswordView,
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    AddReviewView, BookReviewsView, EditReviewView, DeleteReviewView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    # Book Management
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/add/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),

    # Review Management
    path('books/<int:book_id>/reviews/', BookReviewsView.as_view(), name='book_reviews'),
    path('books/<int:book_id>/reviews/add/', AddReviewView.as_view(), name='add_review'),
    path('reviews/<int:pk>/update/', EditReviewView.as_view(), name='edit_review'),
    path('reviews/<int:pk>/delete/', DeleteReviewView.as_view(), name='delete_review'),
]

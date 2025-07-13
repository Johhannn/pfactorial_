from django.urls import path
from .views import (
    RegisterView, CustomAuthToken, LogoutView,
    ProductListCreateView, ProductRetrieveUpdateDestroyView,
    ReviewListCreateView, UserReviewsListView
)

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Products
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    # Reviews
    path('products/<int:product_id>/reviews/', ReviewListCreateView.as_view(), name='product-reviews'),
    path('user/reviews/', UserReviewsListView.as_view(), name='user-reviews'),
]
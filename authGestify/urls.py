from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authGestifyApp import views

urlpatterns = [
    path('login', TokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('user', views.UserCreateView.as_view()),
    path('categories', views.CategoryView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),
    path('user/<int:pk>/products', views.ProductView.as_view()),
    path('user/<int:pk>/providers', views.ProviderView.as_view()),
    path('user/<int:pk>/products/<str:fk>', views.ProductDetailView.as_view()),
    path('user/<int:pk>/providers/<str:fk>', views.ProviderDetailView.as_view()),
]
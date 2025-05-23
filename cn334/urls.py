"""
URL configuration for cn334 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user_management.views import RegisterView, LoginView, UserProfileView, ToggleFavoriteAPIView, FavoriteListAPIView, ProductListAPIView
from product_management import views
from order_management.views import OrderCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('product/all', views.product_all, name='product_all'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('product/summarize', views.product_summary, name='product_summary'),
    path('api/favorite/<str:product_id>/toggle/', ToggleFavoriteAPIView.as_view(), name='toggle_favorite'),
    path('api/favorites/', FavoriteListAPIView.as_view(), name='favorite_list'),
    path('api/products/', ProductListAPIView.as_view(), name='product_list'),
    path('api/orders/', include('order_management.urls')),
    

]

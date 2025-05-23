from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('product_view/<int:pk>/', views.product_view, name='product_view'),
    path('category/<str:foo>', views.category, name='category'),
]

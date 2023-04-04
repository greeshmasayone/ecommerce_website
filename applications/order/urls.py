from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import CartViewSet

router = DefaultRouter()
router.register('cart', CartViewSet, basename='cart')


urlpatterns = [
    path('products/<int:product_id>/wishlist/', views.WishlistView.as_view()),
    path('wishlist/<int:wishlist_pk>/', views.WishlistUpdateView.as_view()),
    path('user/<int:user_id>/address/', views.AddressView.as_view()),
    path('address/<int:address_pk>/', views.AddressUpdateView.as_view()),
    path('cart/', views.CartView.as_view())

]
urlpatterns += router.urls

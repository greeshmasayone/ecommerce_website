from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import CouponViewSet, CreateCheckoutSessionView

router = DefaultRouter()
router.register('coupon', CouponViewSet, basename='cart')

urlpatterns = [
    path('checkout/', CreateCheckoutSessionView.as_view(), name='create_checkout_session')

]
urlpatterns += router.urls

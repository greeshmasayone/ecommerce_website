from audioop import reverse
import stripe
from django.shortcuts import redirect
from rest_framework import generics, status, viewsets
from django.views import View
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import CouponSerializer, PaymentSerializer, RefundSerializer
from .models import Coupon, Payment, Refund
from rest_framework.response import Response
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


class CouponViewSet(viewsets.ModelViewSet):
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated, ]
    search_fields = ["id", "name", "code", "expiry_date", "is_active", "usage_limit", "usage_type", "coupon_type",
                     "value"]
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Coupon.objects.all()
        return queryset


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        host = self.request.get_host()
        # YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'currency': 'inr',
                    'unit_amount': 'amount'*100,
                },
            ],
            mode='payment',
            success_url="http://{}{}".format(host, reverse('order:payment-success')),
            cancel_url="http://{}{}".format(host, reverse('order:payment-cancel')),
            # cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url, code=303)
        # return Response({
        #     'id': checkout_session.id
        # })

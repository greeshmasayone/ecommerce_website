from rest_framework import generics, status, viewsets
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import WishlistSerializer, AddressSerializer, CartSerializer, OrderSerializer
from .models import Cart, Wishlist, Address, Order
from rest_framework.response import Response
from ..customer.models import User
from ..product.models import Product
from django.db.models import Sum, F


class WishlistView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        product_pk = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_pk)
        return product

    def post(self, request, *args, **kwargs):
        serializer = WishlistSerializer(data=request.data)
        product = self.get_object()
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        product_pk = self.kwargs.get('product_id')
        queryset = Wishlist.objects.filter(product=product_pk)
        serializer = WishlistSerializer(queryset, many=True)
        return Response(serializer.data)


class WishlistUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = WishlistSerializer

    def get_object(self):
        wishlist_id = self.kwargs.get('wishlist_pk')
        wishlist = get_object_or_404(Wishlist, id=wishlist_id)
        return wishlist


class AddressView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        user_pk = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_pk)
        return user

    def post(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        user = self.get_object()
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user_pk = self.kwargs.get('user_id')
        queryset = Address.objects.filter(user=user_pk)
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data)


class AddressUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = AddressSerializer

    def get_object(self):
        address_id = self.kwargs.get('address_pk')
        address = get_object_or_404(Address, id=address_id)
        return address


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ]
    search_fields = ['user', 'product', 'product_quantity']
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']

    def get_queryset(self):
        queryset = Cart.objects.filter(user=self.request.user)
        return queryset

    # def cart(request, self):
    #     cart = Cart.objects.annotate(total_cost=Sum(F('product_quantity') * F('self.product.price'))).get(
    #         user=self.request.user
    #     )
    #     cart.total = cart.total_cost
    #     cart.save()


class CartView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        serializer = CartSerializer(data=request.data)
        product = self.get_object()
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        cart_pk = self.kwargs.get('cart_id')
        queryset = Cart.objects.filter(user=self.request.user)
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)

    def cart(self, request):
        cart = Cart.objects.annotate(total_cost=Sum(F('product_quantity') * F('self.product.price'))).get(
            user=self.request.user
        )
        cart.total = cart.total_cost
        cart.save()


class OrderView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        user_pk = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_pk)
        return user

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        user = self.get_object()
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user_pk = self.kwargs.get('user_id')
        queryset = Order.objects.filter(user=user_pk)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

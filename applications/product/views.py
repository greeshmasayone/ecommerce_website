from rest_framework import generics, status
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, CategorySerializer, SubcategorySerializer, GroupSerializer
from .models import Group, Product, Category, SubCategory
from rest_framework.response import Response


class CategoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class SubcategoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        category_pk = self.kwargs.get('category_id')
        category = get_object_or_404(Category, id=category_pk)
        return category

    def get(self, request, *args, **kwargs):
        category_pk = self.kwargs.get('category_id')
        queryset = SubCategory.objects.filter(category=category_pk)
        serializer = SubcategorySerializer(queryset, many=True)
        return Response(serializer.data)


class GroupView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        subcategory_pk = self.kwargs.get('subcategory_id')
        subcategory = get_object_or_404(SubCategory, id=subcategory_pk)
        return subcategory

    def get(self, request, *args, **kwargs):
        subcategory_pk = self.kwargs.get('subcategory_id')
        queryset = Group.objects.filter(subcategory=subcategory_pk)
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        group_pk = self.kwargs.get('group_id')
        group = get_object_or_404(Group, id=group_pk)
        return group

    def get(self, request, *args, **kwargs):
        group_pk = self.kwargs.get('group_id')
        queryset = Product.objects.filter(group=group_pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

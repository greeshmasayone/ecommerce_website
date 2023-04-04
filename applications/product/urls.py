from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('categories/<int:category_id>/subcategories/', views.SubcategoryView.as_view()),
    path('subcategories/<int:subcategory_id>/groups/', views.GroupView.as_view()),
    path('groups/<int:group_id>/products/', views.ProductView.as_view())

]
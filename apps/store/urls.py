from django.urls import path
from . import api, views

urlpatterns = [
    path('api/products', views.product_list),
    path('api/categories', api.get_categories),
    path('api/categories/<slug>', views.category_products),
]

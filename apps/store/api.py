from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Category, Product


def get_categories(request):
    categories = Category.objects.all()
    data = serialize('json', categories)
    print(data)
    return JsonResponse(data, safe=False)


def category_products(request, slug):
    products = Product.objects.filter(category__slug=slug)
    print(products)
    serialized_products = serialize(
        'json', products)
    return JsonResponse(serialized_products, safe=False)

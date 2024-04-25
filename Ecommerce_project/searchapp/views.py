from django.db.models import Q
from django.shortcuts import render
import re

from shop.models import Product

def isnum(s):
    return bool(re.search('[a-zA-Z0-9]', s))

def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        if query.strip():  # Check if query is not empty after stripping whitespace
            if isnum(query):  # Check if query contains alphanumeric characters
                products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))
            else:
                products = Product.objects.none()  # No products if query doesn't contain alphanumeric characters
        else:
            products = Product.objects.none()  # No products if query is empty
    return render(request, 'search.html', {'query': query, 'products': products})

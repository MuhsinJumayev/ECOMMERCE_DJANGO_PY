# apps/products/views.py
from django.shortcuts import render

def get_products(request):
    return render(request, 'products/list.html')
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render

# Create your views here.

def index(request):
    products = Product.objects.all()
#    return HttpResponse('Welcome to Products')
    return render(request,'index.html', {'products': products})


def index1(request):
    return HttpResponse('Welcome to New Products')
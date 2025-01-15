from django.shortcuts import render
from . import models

# Общий список продуктов
def all_products(request):
    if request.method ==  'GET':
        all_products = models.Product.objects.all()
        context = {'all_products': all_products}
        return render(request, template_name='hashtags/all_products.html', context=context)

# Список напитков
def drink_products(request):
    if request.method == 'GET':
        drink_products = models.Product.objects.filter(tags__name='Напитки')
        context = {'drink_products': drink_products}
        return render(request, template_name='hashtags/drink_products.html', context=context)
    
# Список еды
def eat_products(request):
    if request.method == 'GET':
        eat_products = models.Product.objects.filter(tags__name='Еда')
        context = {'eat_products': eat_products}
        return render(request, template_name='hashtags/eat_products.html', context=context)
    
    
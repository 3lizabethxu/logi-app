from itertools import product
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import *
import inventory_app.models
# Create your views here.

def products(request):
    products =  inventory_app.models.Product.objects.all
    return render(request, 'inventory/products.html', {'products':products})

def warehouses(request):
    warehouses =  inventory_app.models.Warehouse.objects.all
    return render(request, 'inventory/warehouses.html',{'warehouses':warehouses})

def createInventory(request):
    
    form = ProductForm()
    if request.method =='POST':
        # print('Printing POST', request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')

    context = {'form':form}
    return render(request, 'inventory/product_form.html',context)

def updateInventory(request, pk):

    product = inventory_app.models.Product.objects.get(name=pk)
    form = ProductForm(instance=product)

    if request.method =='POST':
        # print('Printing POST', request.POST)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products')

    
    context = {'form':form}
    return render(request, 'inventory/product_form.html',context)

def deleteInventory(request, pk):
	product = inventory_app.models.Product.objects.get(name=pk)
	if request.method == "POST":
		product.delete()
		return redirect('/products')

	context = {'product':product}
	return render(request, 'inventory/delete.html', context)













def createWarehouse(request):
    
    form = WarehouseForm()
    if request.method =='POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/warehouses')

    context = {'form':form}
    return render(request, 'inventory/warehouse_form.html',context)

def updateWarehouse(request, pk):

    warehouse = inventory_app.models.Warehouse.objects.get(name=pk)
    form = WarehouseForm(instance=warehouse)

    if request.method =='POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            return redirect('/warehouses')

    
    context = {'form':form}
    return render(request, 'inventory/product_form.html',context)
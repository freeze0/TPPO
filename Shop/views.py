from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import UpdateView
from django.urls import reverse
from .models import *
from Shop.forms import ProductForm
from Shop.forms import CostumerForm


def index(request):
    products = Product.objects.all()
    clients = Client.objects.all()
    orders = Order.objects.all()
    availableproducts = AvailableProduct.objects.all()
    data = {'products': products, 'clients': clients, 'orders': orders, 'availableproducts': availableproducts}
    return render(request, "Shop/index.html", data)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Shop:home'))

    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "Shop/create_product.html", context)

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Shop:home'))
    else:
        form = ProductForm(instance=product)
    return render(request, 'Shop/change_product.html', {'form': form})

def create_costumer(request):
    if request.method == 'POST':
        form = CostumerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Shop:home'))

    form = CostumerForm()
    context = {
        'form': form
    }
    return render(request, "Shop/create_costumer.html", context)

def edit_costumer(request, pk):
    costumer = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = CostumerForm(request.POST, instance=costumer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Shop:home'))
    else:
        form = CostumerForm(instance=costumer)
    return render(request, 'Shop/change_costumer.html', {'form': form})

# class change_product(UpdateView):
#     model = Product
#     template_name = 'Shop/change_product.html'
#     form_class = ProductForm




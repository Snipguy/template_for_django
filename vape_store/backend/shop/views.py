from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})


@login_required
def profile(request):
    orders = request.user.order_set.all()  # or use a related name if defined
    return render(request, 'shop/profile.html', {'orders': orders})

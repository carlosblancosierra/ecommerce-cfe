from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart

# def cart_create(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     print("new cart created")
#     return cart_obj

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {"cart":cart_obj})

def cart_update(request):
    product_id = request.POST.get('product_id')

    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("show messg to user, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)

        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)

    #cart_ob.products.add(product_id)
    #return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")

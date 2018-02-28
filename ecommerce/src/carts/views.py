from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("new cart created")
    return cart_obj


# Create your views here.
def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    # cart_id = request.session.get("cart_id", None)
    # qs = Cart.objects.filter(id=cart_id)
    # if qs.count() == 1:
    #     cart_obj = qs.first()
    #     print("Cart ID exists")
    #     if request.user.is_authenticated and cart_obj.user is None:
    #         cart_obj.user = request.user
    #         cart_obj.save()
    # else:
    #     cart_obj = Cart.objects.new(user=request.user)
    #     request.session['cart_id'] = cart_obj.id

    return render(request, "carts/home.html", {})

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

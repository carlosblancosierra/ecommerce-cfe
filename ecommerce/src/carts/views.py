from django.shortcuts import render
from .models import Cart

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print("new cart created")
    return cart_obj


# Create your views here.
def cart_home(request):


    cart_id = request.session.get("cart_id", None)

    if cart_id is None:
        #print("create new cart")
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id
    else:
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() == 1:
            cart_obj = qs.first()
            print("Cart ID exists")
        else:
            cart_obj = cart_create()
            request.session['cart_id'] = cart_obj.id


    return render(request, "carts/home.html", {})

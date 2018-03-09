from django.shortcuts import render
import stripe

stripe.api_key = 'sk_test_x33KBxusHfdA7eXMyaHdJp6i'
STRIPE_PUB_KEY = 'pk_test_oXY7CAW0bxemHlmDIvnpw4TB'

def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billing/payment-method.html', {"publish_key":STRIPE_PUB_KEY})
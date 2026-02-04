import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Product  # Ensure karein aapka model name 'Product' hi hai

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def create_checkout_session(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # Stripe Checkout Session Create Karna
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'pkr',  # Aap 'usd' bhi kar sakte hain out of country ke liye
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100), # Stripe amount cents mein leta hai
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancel/',
    )
    return redirect(session.url, code=303)
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    # --- SEARCH LOGIC (Step 4) ---
    query = request.GET.get('q') # Home.html ke search input ka naam 'q' hai
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    return render(request, 'home.html', {'products': products})

def create_checkout_session(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # Koyeb ka live URL taake payment ke baad sahi page khule
    domain = "https://minor-valentine-atif-projects-fda25377.koyeb.app"
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'pkr',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100), 
            },
            'quantity': 1,
        }],
        mode='payment',
        # Success aur Cancel URLs ko live domain par set kiya hai
        success_url=domain + '/success/', 
        cancel_url=domain + '/cancel/',
    )
    return redirect(session.url, code=303)
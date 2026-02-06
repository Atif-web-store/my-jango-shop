import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Product

# Stripe key settings se uthayi gayi hai
stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    """
    Step 4: Search functionality logic.
    Ye logic home page par products ko filter karti hai.
    """
    query = request.GET.get('q') # 'q' search input ka naam hai jo home.html mein hai
    
    if query:
        # Agar user search kare toh matching products dikhao
        products = Product.objects.filter(name__icontains=query)
    else:
        # Warna saare products dikhao
        products = Product.objects.all()
    
    return render(request, 'home.html', {'products': products})

def signup(request):
    """
    Naye users ke liye account banane ki logic.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Signup ke baad khud ba khud login ho jayega
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def create_checkout_session(request, product_id):
    """
    Step 4: Professional Payment Flow.
    Live domain URLs set kiye gaye hain taake error na aaye.
    """
    product = Product.objects.get(id=product_id)
    
    # Aapka live Koyeb URL
    domain = "https://minor-valentine-atif-projects-fda25377.koyeb.app"
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'pkr',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': int(product.price * 100), # Amount cents mein convert ki gayi hai
            },
            'quantity': 1,
        }],
        mode='payment',
        # Payment ke baad in paths par redirect hoga
        success_url=domain + '/success/', 
        cancel_url=domain + '/cancel/',
    )
    return redirect(session.url, code=303)
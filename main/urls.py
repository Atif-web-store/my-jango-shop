from django.urls import path, include
from . import views
from django.shortcuts import render

urlpatterns = [
    # Home Page aur Search logic
    path('', views.home, name='home'),
    
    # User Authentication (Signup aur Login)
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Stripe Payment ka rasta
    path('buy/<int:product_id>/', views.create_checkout_session, name='buy'),
    
    # Success, Cancel aur Documentation ke raste
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    path('cancel/', lambda request: render(request, 'cancel.html'), name='cancel'),
    path('documentation/', lambda request: render(request, 'documentation.html'), name='docs'),
]
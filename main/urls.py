from django.urls import path
from . import views
from django.shortcuts import render # Ye zaroori hai

urlpatterns = [
    path('', views.home, name='home'),
    path('buy/<int:product_id>/', views.create_checkout_session, name='buy'),
    
    # Ye do lines laazmi add karein taake payment flow mukammal ho
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    path('cancel/', lambda request: render(request, 'cancel.html'), name='cancel'),
]
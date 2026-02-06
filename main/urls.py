from django.urls import path, include
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')), # Login/Logout handles
    path('buy/<int:product_id>/', views.create_checkout_session, name='buy'),
    
    # Success, Cancel aur Documentation ke raste
    path('success/', lambda request: render(request, 'success.html'), name='success'),
    path('cancel/', lambda request: render(request, 'cancel.html'), name='cancel'),
    path('documentation/', lambda request: render(request, 'documentation.html'), name='docs'),
]
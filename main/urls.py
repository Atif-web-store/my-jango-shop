from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buy/<int:product_id>/', views.create_checkout_session, name='buy'),
]
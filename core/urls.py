from django.urls import path, include
from .views import (
    add_to_cart,
    remove_from_cart,
    CheckoutView,
    HomeView,
    OrderSummary,
    ItemDetailView,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummary.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>',add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/',PaymentView.as_view(),name='payment'),
    path('add-coupon/',AddCouponView.as_view(), name='add-coupon'),
]
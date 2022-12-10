from django.urls import path
from .views import CartItem

urlpatterns = [
    # not a view in gui sense -- a request handler.
    path('cart-items/', CartItemViews.as_view())
]
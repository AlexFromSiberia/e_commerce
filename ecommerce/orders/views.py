from django.http.response import JsonResponse
from basket.basket import Basket
from .models import Order, OrderItem


def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        user_id = request.user.id
        baskettotal = basket.get_total_price()
        full_name = 'full_name'  # request.POST.get('full_name')
        address1 = 'address_line_1'  # request.POST.get('address_line_1')
        address2 = 'address_line_1'   # request.POST.get('address_line_1')

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            # TODO: replace static "name" and "addr" with form data
            order = Order.objects.create(user_id=user_id, full_name=full_name, address1=address1,
                                address2=address2, total_paid=baskettotal, order_key=order_key)
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        response = JsonResponse({'success': 'Return something'})
        return response


def payment_confirmation(data):
    """Confirms billing status"""
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    """Returns list of orders a user made"""
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders

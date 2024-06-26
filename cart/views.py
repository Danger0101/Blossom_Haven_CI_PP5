from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ A view that renders the cart contents page """
    cart = request.session.get('cart', {})
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        if product.inventory.quantity == 0:
            messages.warning(request, (
                f'The item "{product.name}" '
                'in your cart is now out of stock.'))
        elif quantity > product.inventory.quantity:
            messages.warning(request, (
                f'You have added more "{product.name}" '
                'to your cart than currently available in stock.'))

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity <= 0:
        messages.error(request, 'Quantity must be greater than zero.')
        return redirect(redirect_url)

    if product.inventory.quantity == 0:
        messages.error(request, 'This product is currently out of stock.')
        return redirect(redirect_url)
    elif product.inventory.quantity < quantity:
        messages.error(request, (
            f'Only {product.inventory.quantity} items available in stock.'))
        return redirect(redirect_url)

    if item_id in cart:
        new_quantity = cart[item_id] + quantity
        if new_quantity > product.inventory.quantity:
            messages.error(request, (
                f'Cannot add more items. Only {product.inventory.quantity}'
                ' available in stock.'))
            return redirect(redirect_url)
        cart[item_id] = new_quantity
        messages.success(request, (
            f'Updated {product.name} quantity to {cart[item_id]}'))
    else:
        if quantity > product.inventory.quantity:
            messages.error(request, (
                f'Cannot add more items. Only {product.inventory.quantity}'
                ' available in stock.'))
            return redirect(redirect_url)
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity < 0:
        messages.error(request, 'Quantity cannot be negative.')
        return redirect(reverse('view_cart'))

    if quantity > product.inventory.quantity:
        messages.error(request, (
            f'Cannot adjust quantity. Only {product.inventory.quantity}'
            ' available in stock.'))
        return redirect(reverse('view_cart'))

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, (
            f'Updated {product.name} quantity to {cart[item_id]}'))
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

from .basket import Basket

# display data/items in basket (quantity of items in basket)
def basket(request):
    return {'basket': Basket(request)}
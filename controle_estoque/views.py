from django.shortcuts import render
from Estoque.models import StockItem

def stock_item_list(request):
    stock_items = StockItem.objects.all()
    context = {'stock_items': stock_items}
    return render(request, 'controle_estoque/stock_item_list.html', context)

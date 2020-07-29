from django.urls import path

from quotes.views import quotes, oanda, new, add_stock, delete, delete_stock

urlpatterns = [
    path('quotes/', quotes, name='quotes'),
    path('oanda/', oanda, name='oanda'),
    path('new/', new, name='new'),
    path('add_stock/', add_stock, name='add_stock'),
    path('delete/<stock_id>', delete, name="delete"),
    path('delete_stock/', delete_stock, name="delete_stock"),
]
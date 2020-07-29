from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock

from .forms import StockForm
# Create your views here.

def quotes(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_requests = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_e218d1e951cf4c7d8c3124310f14f993")

        try:
        	api = json.loads(api_requests.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'quotes.html', {'api': api})

    else:
        return render(request, 'quotes.html', {'ticker': "Enter A Ticker to Start"})



    #Public API(iexcloud.io): pk_e218d1e951cf4c7d8c3124310f14f993

def oanda(request):
    return render(request, 'oanda.html', {})

def new(request):
    return render(request, 'new.html', {})

def add_stock(request):
	import requests
	import json
        
	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock Has Been Added"))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		output = []
		for ticker_item in ticker:
			api_requests = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_e218d1e951cf4c7d8c3124310f14f993")

			try:
				api = json.loads(api_requests.content)
				output.append(api)
			except Exception as e:
				api = "Error..."

		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock has been deleted!"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker': ticker})

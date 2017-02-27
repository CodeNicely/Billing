from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from user_details.models import user_data
from Order_item.models import Order_item
# Create your views here.


@csrf_exempt
def place_orders(request):
	if request.method=='GET':
		render(request,"place_orders.html",{})
	else:
		customer_name=request.POST.get("customer_name")
		price=request.POST.get("price")
		quantity = request.POST.get("quantity")
		item_name = request.POST.get("item_name")
		
		print customer_name,price,quantity,item_name

		i=1;

		 
 
	return render(request,"place_orders.html",{})

		




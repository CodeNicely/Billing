from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from user_details.models import user_data
from order.models import order_data_purchase
from item.models import item_data
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
		
		total = float(quantity)*float(price)

		i=1;

		print total

		id_from_itemtable=request.objects.get()

		order_data_purchase.objects.create(order_id=i,customer_name=customer_name,sub_total=total)
		rder_item.objects.create(order_id=1)

		

		Order_item.objects.create(order_id=i)
 
	return render(request,"place_orders.html",{})

		




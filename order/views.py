from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from user_details.models import user_data
from order.models import order_data_purchase
from item.models import item_data
import random
# Create your views here.


@csrf_exempt
def place_orders(request):
	if request.method=='GET':
		render(request,"place_orders.html",{})
	else:
		customer_name=request.POST.get("customer_name")
		
		total = float(quantity)*float(price)

		rand = random.randint(100,999)
		order_id = "BS"+str(rand)

		print order_id


		item_list=item_data.objects.values_list(item_name)
		print item_list

 
	return render(request,"place_orders.html",{})



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

		print customer_name

	return render(request,"place_orders.html",{})



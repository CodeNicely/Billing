from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def order_home(request):
	if request.method=='GET':
		return render(request,"orders.html",{})		
		
	else:
		customer_id=request.POST.get("customer_name")
		order_type = request.POST.get("order_type")

		print customer_id,order_type


		try: 
			customer_from_db = order_data.objects.get(customer_name=customer_id)
			order_type_db = order_data.objects.get(order_type=order_type)


			if customer_from_db.customer_name==customer_id and order_type_db.order_type==order_type:
				info = order_data.objects.all()

				print "hello"
				print info
				print str(info)
				print len(info)

				return render(request,"testing.html",{"info":info})
				
				
		except Exception,e:
			print "Error"

		



def testing(request):
	return render(request,"other_order.html",{})
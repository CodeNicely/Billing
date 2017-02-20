from django.shortcuts import render

# Create your views here.


def order_home(request):
	if request.method=='GET':
		return render(request,"orders.html",{})		
		
	

		
		
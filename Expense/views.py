from django.shortcuts import render 
from Expense.models import *
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def expense(request):
	if request.method=='GET':
		return render(request,"expense.html",{})

	else:

		title=request.POST.get("title");
		description=request.POST.get("description");
		amount=request.POST.get("amount");


		expense_data.objects.create(title=title,description=description,amount=amount)

		data=expense_data.objects.all()



		expense_array=[] 

		for x in data:
			expense_object={}
			expense_object["title"]=x.title
			expense_object["description"]=x.description
			expense_object["amount"]=x.amount
			expense_array.append(expense_object)			



		sumq=expense_data.objects.aggregate(Sum('amount'))

		print sumq

		return render(request,"expense.html",{ "expense_array": expense_array })




import json
from django.shortcuts import render 
from Expense.models import *
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def add_expense(request):
	if request.method=='GET':
		return render(request,"add_expense.html",{})

	else:

		title=request.POST.get("title");
		description=request.POST.get("description");
		amount=request.POST.get("amount");


		expense_data.objects.create(title=title,description=description,amount=amount)

		# data=expense_data.objects.all()



		# expense_array=[] 

		# for x in data:
		# 	expense_object={}
		# 	expense_object["title"]=x.title
		# 	expense_object["description"]=x.description
		# 	expense_object["amount"]=x.amount
		# 	expense_array.append(expense_object)

		# data = json.dumps(expense_array)


		# sumq=expense_data.objects.aggregate(Sum('amount'))



		return render(request,"add_expense.html",{})



#"expense_array": data



def show_expense(request):

	start_date=request.POST.get("start_date")
	end_date=request.POST.get("end_date")

	filtered_data = expense_data.objects.filter(created__range=["start_date", "end_date"])



	data=expense_data.objects.all()
	expense_array=[]
	for x in data:
		expense_object={}
		expense_object["title"]=x.title
		expense_object["description"]=x.description
		expense_object["amount"]=x.amount
		expense_object["created"]=str(x.created)
	#	expense_object["created"]=expense_object["created"][0:16]
		expense_object["modified"]=str(x.modified)
	#	expense_object["modified"]=expense_object["modified"][0:16]
		expense_array.append(expense_object)
	data = json.dumps(expense_array)

	sumq=expense_data.objects.aggregate(Sum('amount'))
	return render(request,"show_expense.html",{"expense_array": data})



# def filter_data(request):
# 	start_date=str(request.POST.get("start_date"));
# 	end_date=str(request.POST.get("end_date"));

# 	filtered_data = expense_data.objects.filter(date__range=["start_date", "end_date"])

# 	filtered_array=[]

# 	for x in filtered_data:
# 		filtered_object={}
# 		filtered_object["title"]=x.title
# 		filtered_object["description"]=x.description
# 		filtered_object["amount"]=x.amount
# 		filtered_object["created"]=x.created
# 		filtered_object["modified"]=x.modified
# 		filtered_array.append(filtered_object)

# 	data2=json.dumps(filtered_array)



# 	return render(request,"show_expense.html",{"filtered_array" : data2 })



def testing1(request):
	return render(request,"testing.html",{})
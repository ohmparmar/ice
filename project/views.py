from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import redirect
from project.models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect

# Create your views here.
#user id :manager1@janta.com
#password: Ajay@12345
@csrf_exempt
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            return render(request,'login.html')
    # No backend authenticated the credentials


    return render(request,'login.html')

def dashboard(request):
    if request.user.is_authenticated:   
        return render(request,'dashboard.html')
    else:
        return redirect("/")
    #return render(request,'dashboard.html')

def landing(request):
    return render(request,'landing.html')


def logoutuser(request):
    logout(request)
    return redirect("/login")

@csrf_exempt
def purchase(request):
    if request.method=="POST":
        print("hello")
        outlet_PID=request.POST.get("outlet_PID")
        outlet_ID=request.POST.get("outlet_ID")
        icecream_ID=request.POST.get("icecream_ID")
        quantity_of_Purchase=request.POST.get("quantity_of_purchase")
        Date_time1=request.POST.get("date_time2")
        outlet_purchase1=Outlets_Purchase(outlet_PID=outlet_PID,outlet_ID_id=outlet_ID,
        icecream_ID_id=icecream_ID,quantity_of_purchase=quantity_of_Purchase,date_time1=Date_time1)
        outlet_purchase1.save()
        allinfo= Outlets_Purchase.objects.all()
        context={"allinfo":allinfo}
        return render(request,'purchase.html',context)

    elif request.user.is_authenticated: 
        print("inside request.user block")
        allinfo= Outlets_Purchase.objects.all()
        context={"allinfo":allinfo} 
        return render(request,'purchase.html',context)

    else:
        return redirect("/")


def stocks(request):
    if request.user.is_authenticated:   
        return render(request,'stocks.html')
    else:
        return redirect("/")

def sales(request):
    if request.method=="POST":
        print("request method from sales post recived")
        outlet_SID=request.POST.get("outlet_SID")
        outlet_ID=request.POST.get("outlet_ID")
        icecream_ID=request.POST.get("icecream_ID")
        units_sold=request.POST.get("units_sold")
        date_time2=request.POST.get("date_time2")
        print(date_time2)
        outlet_sales=Outlet_Sales(outlet_SID=outlet_SID,outlet_ID_id=outlet_ID,
        icecream_ID_id=icecream_ID,units_sold=units_sold,date_time2=date_time2)
        outlet_sales.save()
        allinfo= Outlet_Sales.objects.all()
        context={"allinfo":allinfo}
        return render(request,'sales.html',context)

    elif request.user.is_authenticated:   
        allinfo= Outlet_Sales.objects.all()
        context={"allinfo":allinfo} 
        return render(request,'sales.html',context)
        

    
    else:
        return redirect("/")
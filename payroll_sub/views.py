from django.shortcuts import render,redirect
from . models import *
from django.urls import path
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.db.models import Sum
from . serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse

# Create your views here.
#localhost:8000/employeapi/
#localhost:8000/employeapi/id
@csrf_exempt
def info(request):
    if request.method == 'GET':
        sendnow = Employees.objects.all()
        serializer = Fetchserializer(sendnow,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Fetchserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def sendmoneydetail(request,pk):
    try:
        onsend = Employees.objects.get(pk=pk)
    except Employees.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = Fetchserializer(onsend)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Fetchserializer(onsend, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.data, status = 400)

    elif request.method == "DELETE":
        onsend.delete()
        return HttpResponse(status = 201)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect("home")
        else:
            messages.error(request,"Invalid username or password.")
    return render(request, 'index.html')

def logout(request):
    logout(request)
    return redirect('logout')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
@login_required(login_url='login')
def payment(request):
    selectall = Payment.objects.all()
    update = Payment.objects.get(id=1)
    if request.method == 'POST':
        update.account = request.POST['balance']
        update.save()
    return render(request,'payments.html',{'data':selectall})

@login_required(login_url='login')
def paydate(request):
    selectall = Payment.objects.all()
    update = Payment.objects.get(id=1)
    if request.method == 'POST':
        update.payment_date = request.POST['date']
        update.save()
    return render(request, 'paydate.html',{'data':selectall})

@login_required(login_url='login')
def payemployee(request):
    selectdata = Employees.objects.all()
    detail = Employees.objects.aggregate(thedata=Sum('salary'))
    return render(request, 'payemployee.html',{'data':selectdata,"dsum":detail})

@login_required(login_url='login')
def addemployee(request):
    if request.method == 'POST':
        data = Employees()
        data.fname = request.POST['firstname']
        data.lname = request.POST['lastname']
        data.dob = request.POST['dob']
        data.gender = request.POST['gender']
        data.phonenumber = request.POST['phonenumber']
        data.email = request.POST['email']
        data.address = request.POST['address']  
        data.image = request.FILES['image']   
        data.branch = request.POST['branch']
        data.destination = request.POST['designation']
        data.department = request.POST['department']
        data.joineddate = request.POST['joindate']
        data.salary = request.POST['salary']
        data.assurance = request.POST['assurance']
        data.bankaccountno = request.POST['bankaccountno'] 
        data.save()         
    return render(request, 'addemployee.html')

@login_required(login_url='login')
def employees(request):
    selectall = Employees.objects.all()
    return render(request, 'employees.html',{"data":selectall})

@login_required(login_url='login')
def view(request,id):
    selectall = Employees.objects.get(id=id)
    return render(request,'view.html',{"data":selectall})

@login_required(login_url='login')
def delete_employee(request,id):
    selectall = Employees.objects.get(id=id)
    selectall.delete()
    return redirect('employees')

@login_required(login_url='login')
def edit(request,id):
    selectone = Employees.objects.get(id=id)
    if request.method == 'POST':
        selectone.fname = request.POST['firstname']
        selectone.lname = request.POST['lastname']
        selectone.dob = request.POST['dob']
        selectone.gender = request.POST['gender']
        selectone.phonenumber = request.POST['phonenumber']
        selectone.email = request.POST['email']
        selectone.address = request.POST['address']  
        selectone.image = request.FILES['image']   
        selectone.branch = request.POST['branch']
        selectone.destination = request.POST['designation']
        selectone.department = request.POST['department']
        selectone.joineddate = request.POST['joindate']
        selectone.salary = request.POST['salary']
        selectone.assurance = request.POST['assurance']
        selectone.bankaccountno = request.POST['bankaccountno'] 
        savedata =  selectone.save() 
        if savedata is not None:
            return redirect('employees')

    return render(request,'editemployee.html',{"data":selectone})

@login_required(login_url='login')
def message(request):
    return render(request, 'message.html')

@login_required(login_url='login')
def sendmessage(request):
    selectall = Message.objects.all()
    return render(request, 'sendmessage.html',{"data":selectall})

@login_required(login_url='login')
def composemessage(request):
    if request.method == 'POST':
        to = request.POST['to']
        title = request.POST['title']
        body = request.POST['body']
        Message(title=title,body=body,sender='jeannineuwiringiyimana2@gmail.com',receiver=to,datetime=timezone.now()).save()
        send_mail(
            title,
            body,
            'settings.EMIAL_HOST_USER',
            [to],
            fail_silently=True
        )
    return render(request, 'composemessage.html')

@login_required(login_url='login')
def setting(request):
    return render(request, 'setting.html')

@login_required(login_url='login')
def adddepartment(request):       
    return render(request, 'adddepartment.html')

@login_required(login_url='login')
def departments(request):
    selectall = Department.objects.all()
    arg = {"user":request.user}
    if request.method == 'POST':
        de = Department()
        de.depart_name = request.POST['dept']
        de.last_update_by = user.username
        de.last_updated = timezone.now()
        de.save()
    return render(request, 'departments.html',{'data':selectall})

@login_required(login_url='login')
def addbranch(request):
    return render(request, 'addbranch.html')

@login_required(login_url='login')
def branches(request):
    return render(request, 'branches.html')

@login_required(login_url='login')
def changepassword(request):
    return render(request, 'changepassword.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')


@csrf_exempt
def messagess(request):
    if request.method == 'GET':
        sendnow = Message.objects.all()
        serializer = Getserializer(sendnow,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Getserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)





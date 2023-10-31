from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.urls import reverse
from Future.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Future.decorators import unathen_user,allowed_users,unathen_admin
import razorpay 
from django.conf import settings
# Create your views here.

#Front End For customers starts
# Home Page 
def home(request):
    submit=None
    course=Course.objects.all()
    print(i.photo for i in course)
    data=request.GET.get('data')
    if request.method=="POST":
        email=request.GET.get('email')
        print(email)
        if email:
            check=Leads.objects.filter(email=email)
            if check:
                pass
            else:
                x=Leads.objects.create(name=name,email=email)
                x.save()
                submit=1
                url=reverse('home')
                red=f'{url}?data={name}'
                return redirect(red)
    print(submit)
    return render(request,'home.html',{'submit':data,'course':course})

# Course Page 
def course(request,pk):
    course_det=Course.objects.filter(pk=pk)
    # print(course_det)
    y=(p.highlight for p in course_det)
    high=[(i.highlight).split('/n') for i in course_det]
    # print(high)
    x=high[0]
    print(x)
    return render(request,'course.html',{'course':course_det,'highlight':x})
# Register Page 
def register(request,pk):
    
    course=Course.objects.filter(pk=pk)
    form=registerForm()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        course_id=pk
        client=Client.objects.filter(email=email)
        client_ph=Client.objects.filter(phone=phone)
        course_inf=Course.objects.filter(id=course_id)
        if form.is_valid:
            if client:
                               
                return render(request,'register.html',{'form':form,'email':email})
            elif client_ph:
                              
                return render(request,'register.html',{'form':form,'phone':phone})
                
            else:
                x=Client.objects.create(name=name,email=email,phone=phone)
                x.save()
                return redirect(f'/payment/'+str(course_id))                
        else:
            print('Ritik')
    context={
            'form':form,
        }
    return render(request,'register.html',context)

def pay(request,pk):
    course_id=pk
    course=Course.objects.filter(id=pk)
    price=[i.price for i in course]
    client = razorpay.Client(auth=(settings.KEYID, settings.SECRETKEY))
    data = { "amount": (price[0])*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    print(payment)
    context={
        'payment':payment,
    }
    return render(request,'payment.html',context)
def success(request):
    return HttpResponse('success')

#Front End For customers ends


#Front End For Student starts

@unathen_user #This is custom decorator to check user is logged in or not
def stu_register(request):
    form=UserCreationForm()
    if request.method=='POST': 
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"account is created")
    return render (request,'stu_register.html',{'form':form})
@unathen_user
def stu_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            request.session
            #this will login to admin control pannel
            return redirect('stu_login')
        else:
            error_msg='Invalid username or Password'
            return render(request,'stu_login.html',{'error':error_msg})
    return render(request,'stu_login.html')
def logout_stu(request):
    logout(request)
    #This will logout the user
    return redirect('stu_login')
@allowed_users(allowed_roles=['Student'])
def stu_portal(request):
    return render(request,'stu_portal.html')

#Student Portal Ends


#Admin Pannel Starts

@login_required(login_url='admin_login')
@allowed_users(allowed_roles=['User_adm'])
def admin_home(request):
    leads=Leads.objects.all()
    context={
        'leads':leads
    }
    return render (request,'admin_home.html',context)
@unathen_admin
def login_admin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            #this will login to admin control pannel
            return redirect('admin_home')
    return render(request,'admin_login.html')
            
def logout_admin(request):
    logout(request)
    #This will logout the user
    return redirect('admin_login')

@login_required(login_url='admin_login')
@allowed_users(allowed_roles=['User_adm'])
def course_manage(request):
    courses=Course.objects.all()
    form=coourse_edit()
    if request.method=="POST":
        category=request.POST.get('category')
        desc=request.POST.get('desciption')
        high =request.POST.get('highlight')
        prc =request.POST.get('price')
        photo  =request.POST.get('photo')
        if category:
            x=Course.objects.create(category=category,description=desc,highlight=high,price=prc,photo=photo)
            x.save()
            redirect('course_manage')
    context={
        'courses':courses ,
        'form':form
    }
    return render(request,'course_manage.html',context)
@login_required(login_url='admin_login')
@allowed_users(allowed_roles=['User_adm'])
def edit_course(request,pk):
    my_model_instance = Course.objects.get(pk=pk)
    form = coourse_edit(instance=my_model_instance)
    if request.method == 'POST':
        form = coourse_edit(request.POST, instance=my_model_instance)
        if form.is_valid():
            form.save()
            print('ritik')
            return redirect('course_manage')
    print(my_model_instance.photo)
    # form=coourse_edit()
    return render(request, 'edit_course.html', {'form': form,'course':my_model_instance})

@login_required(login_url='admin_login')
@allowed_users(allowed_roles=['User_adm'])
def student_manage(request):
    students=Student.objects.all()
    return render(request,'student_manage.html',{'students':students})

@login_required(login_url='admin_login')
@allowed_users(allowed_roles=['User_adm'])
def content_manage(request):
    videos=Course_content.objects.all()
    return render(request,'content_manage.html',{'videos':videos})    
# Admin Panel Ends 
 
def index(request):
    return render(request,'new.html')
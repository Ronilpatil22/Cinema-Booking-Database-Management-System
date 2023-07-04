from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from home2.models import contact,email_id,ticket
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,logout
from paypal.standard.forms import PayPalPaymentsForm
from decimal import Decimal
from django.conf import settings
import uuid
from django.urls import reverse
# Create your views here.

def movies(request):

    return render(request,'movies.html')

def home(request):
    return render(request,'index.html')

def contact_us(request):
    researcher = ''
    study = ''

    if request.method=="POST":
        First_name=request.POST.get('First_name')
        Last_name=request.POST.get('Last_name')
        Email_id=request.POST.get('Email_id')
        Mobile_number=request.POST.get('Mobile_number')
        Message=request.POST.get('Message')
        Contact=contact(First_name=First_name,Last_name=Last_name,Email_id=Email_id,Mobile_number=Mobile_number,Message=Message,date=datetime.today())
        Contact.save()
        messages.success(request, 'Your message has been sent.')
        
    return render(request,"Contact_Us.html")
    
def handleSignup(request):
    researcher = ''
    study = ''

    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        if len(username)>10:
            messages.warning(request, "Username must be under 10 characters")
            return redirect('login.html')
        
        if not username.isalnum():
            messages.warning(request, "Username can only contain Letters and Numbers")
            return redirect('login.html')
        
        if pass1 != pass2:
            messages.warning(request, "Passwords do not match")
            return redirect('login.html')
        
        user = User.objects.create(username=username,email=email,password=make_password(pass1))
        user.save()
        
        # if user.objects.filter(username = username).first():
        #     messages.success(request, "This username is already taken")
        #     return redirect('login.html')
        
        # print(user.email)
        
        messages.success(request, " Your CineShow account has been succesfully created ")
        return redirect('login.html')
    
    
    else:
        return HttpResponse('404 - Error Not found')
    
def signup(request):
    
    return render(request,'signup.html')

def about(request):
    researcher = ''
    study = ''
    
    if request.method=="POST":
        email=request.POST.get('email')
        Email_id=email_id(email=email,date=datetime.today())
        Email_id.save()
        
    return render(request,"about.html")

def book(request):
    return render(request,"ticket-booking.html")

def seat(request):
    return render(request,"seat_sel.html")
    
def payment(request):
    if request.method=="POST":
        # price=request.POST.get('price','')
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        
        Ticket=ticket(date=date,time=time)
        Ticket.save()
        return redirect('ticket-booking')

def handleLogin(request):
    researcher = ''
    study = ''
    
    if request.method=="POST":
        signinname=request.POST.get('signinname')
        signinpasswd=request.POST.get('signinpasswd')
        
        User=authenticate(username=signinname,password=signinpasswd)
        
        if User is not None:
            login(request,User)
            messages.success(request,"You have successfully logged in")
            return redirect('home')
        else:
            messages.warning(request,"Invalid credentials, Please Try Again!")
            return redirect('login.html')
    else:
        return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')
    
    return render(request,'movies.html')

def book(request):
    researcher = ''
    study = ''
    
    if request.method=="POST":
        movie_name=request.POST.get('movie_name')
        
        Ticket=ticket(username=request.user,movie=movie_name,date='2000-03-04',seat='A2',screen='1',price='203')
        Ticket.save()
        
        if not User.is_authenticated:
            messages.warning(request,'Login to get your tickets on your whatsapp')
    return render(request,'ticket-booking.html')

def paypal(request):
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '10000.00',
        'item_name': 'order',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'INR',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("book")}',
        'cancel_return': f'http://{host}{reverse("home")}',
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form' : form}
    return render(request,"paypal.html" ,context)


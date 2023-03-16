from django.shortcuts import render
import os
import uuid

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.core.mail import send_mail

from project.settings import EMAIL_HOST_USER



# Create your views here.


def user(request):
    if request.method == 'POST':
        a = userlog(request.POST)
        if a.is_valid():
            em = a.cleaned_data['username']
            passw = a.cleaned_data["password"]
            b = usermodel.objects.all()  # use to fetch all data
            for i in b:  # use to visit in each row in regmodel
                if em == i.username and passw == i.password:
                    ii = i.id
                    return redirect(f'/user_profile/{em}/{ii}')
            else:
                return HttpResponse("Login Failed")
    return render(request, 'user.html')


def shop(request):
    if request.method == 'POST':
        a = shoplog(request.POST)
        if a.is_valid():
            em = a.cleaned_data['username']
            passw = a.cleaned_data["password"]
            b = shopmodel.objects.all()
            user_obj = shopmodel.objects.filter(username=em).first()
            if user_obj is None:  # if user doesn't exist
                messages.success(request, 'user not found')
                return redirect(shop)
            profile_obj = shopmodel.objects.filter(username=user_obj).first()
            if not profile_obj.is_verified:  # if not  profile is false
                messages.success(request, 'profile not verified check your mail')
                return redirect(shop)
            # user= authenticate(username=em,password=passw)
            # user=valid
            # if the given credentials are valid,return a User object
            # if user is None:
            #     messages.success(request,'wrong password or username')
            #     return redirect(shop)
            for i in b:  # use to visit in each row in regmodel
                if em == i.username and passw == i.password:
                    ii= i.id
                    return redirect(f'/profile/{em}/{ii}')
            else:
                messages.success(request,'wrong password or username')
                return redirect(shop)
    return render(request, 'shop.html')


def userreg(request):
    if request.method=='POST':
        a=userform(request.POST)
        if a.is_valid():
            us=a.cleaned_data["username"]
            em=a.cleaned_data["email"]
            passw=a.cleaned_data["password"]
            cpass=a.cleaned_data['cpassword']
            if cpass==passw:
                b=usermodel(username=us,email=em,password=passw)
                if usermodel.objects.filter(username=us).first():
                    # it will get   first object from filter query
                    messages.success(request, 'username already taken')
                    return redirect(userreg)
                if usermodel.objects.filter(email=em).first():
                    messages.success(request, 'email already exist')
                    return redirect(userreg)
                b.save()
                return redirect(user)
            else:
                return HttpResponse("registraion failed")
        else:
            return HttpResponse("registraion failed")
    return render(request,'signup.html')



def shopreg(request):
    if request.method=='POST':
        a=shopform(request.POST)
        if a.is_valid():
            us=a.cleaned_data["username"]
            em=a.cleaned_data["email"]
            passw=a.cleaned_data["password"]
            cpass=a.cleaned_data['cpassword']
            if cpass==passw:
                if shopmodel.objects.filter(username=us).first():
                    # it will get   first object from filter query
                    messages.success(request, 'username already taken')
                    return redirect(shopreg)
                # if usermodel.objects.filter(email=em).first():
                #     messages.success(request, 'email already exist')
                #     return redirect(shopreg)
                auth_token = str(uuid.uuid4())
                b=shopmodel(username=us,email=em,auth_token=auth_token,password=passw)
                b.save()
                send_mail_regis(em,auth_token)    # mail sending function
                return redirect(shop)
            else:
                return HttpResponse("registraion failed")
    return render(request,'signupp.html')
#
#
#
def send_mail_regis(email,auth_token):
    subject="your account has been verified"
    message=f'paste the link to verify your account http://127.0.0.1:8000/verify/{auth_token}'
    email_from=EMAIL_HOST_USER     # from
    recipient=[email]    #to
    send_mail(subject,message,email_from,recipient)
#
#
def verify(request,auth_token):
    profile_obj=shopmodel.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:  #if profile object is false
            messages.success(request,'your account is already verified')
            return redirect(shop)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(shop)
    else:
        messages.success(request,'user not found')
        return redirect(shop)



def index(request):
    return render(request,'index.html')
def demo(request):
    return render(request,'demo.html')
def address(request):
    return render(request,'address.html')
def orderplaced(request):
    return render(request,'orderplaced.html')

def profile(request,username,id):
    return render(request,'profile.html',{'x':username,'y':id})

def userprofile(request,username,id):
    x = productmodel.objects.all()
    li = []
    nm = []
    pr = []
    des = []
    iid = []
    for i in x:
        a = i.image
        li.append(str(a).split('/')[-1])
        b = i.pname
        nm.append(b)
        c = i.price
        pr.append(c)
        d = i.description
        des.append(d)
        e = i.id
        iid.append(e)
    mylist = zip(li, nm, pr, des, iid)
    return render(request, 'user_profile.html', {'x': username, 'y': id,'mylist': mylist})

def edituser(request,id):
    a = usermodel.objects.get(id=id)
    x=a.username
    y=a.id
    z=a.email
    if request.method == 'POST':
        a.username = request.POST.get('name')
        a.email = request.POST.get('email')
        a.password = request.POST.get('password')
        cp=request.POST.get('cpassword')
        if a.password==cp:
            a.save()
            em=a.username
            ii=a.id
            return redirect(f'/user_profile/{em}/{ii}')
        else:
            return HttpResponse("failed")
    return render(request,'edit_user.html',{'x':x,'y':y,'z':z})

def upload_product(request,id):
    c=shopmodel.objects.get(id=id)
    x=c.username
    y=c.id
    if request.method == 'POST':
        a = productform(request.POST, request.FILES)
        if a.is_valid():
            nm = a.cleaned_data['pname']
            pid = a.cleaned_data['pid']
            pr = a.cleaned_data['price']
            des = a.cleaned_data['des']
            im = a.cleaned_data['image']
            b = productmodel(pname=nm, pid=pid, price=pr, description=des, image=im)
            b.save()
            return redirect(f'/profile/{x}/{y}')
        else:
            return HttpResponse("item addedd failed")
    return render(request, 'upload_product.html',{'x':x,'y':y})


def editshop(request,id):
    a = shopmodel.objects.get(id=id)
    x=a.username
    y=a.id
    if request.method == 'POST':
        a.username = request.POST.get('name')
        a.email = request.POST.get('email')
        a.password = request.POST.get('password')
        cp=request.POST.get('cpassword')
        if a.password==cp:
            a.save()
            em=a.username
            ii=a.id
            return redirect(f'/profile/{em}/{ii}')
        else:
            return HttpResponse("failed")
    return render(request,'edit_profile.html',{'x':x,'y':y})


def productdisplay(request):
    x=productmodel.objects.all()
    li=[]
    nm=[]
    pr=[]
    des=[]
    id=[]
    for i in x:
        a=i.image
        li.append(str(a).split('/')[-1])
        b=i.pname
        nm.append(b)
        c=i.price
        pr.append(c)
        d=i.description
        des.append(d)
        e=i.id
        id.append(e)
    mylist=zip(li,nm,pr,des,id)
    return render(request,'product_display.html',{'mylist':mylist})

def editproduct(request,id):
    a=productmodel.objects.get(id=id)
    nm=a.pname
    pr=a.price
    de=a.description
    im=str(a.image).split('/')[-1]
    if request.method=='POST':
        if len(request.POST)>0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.pname=request.POST.get('pname')
        a.price=request.POST.get('price')
        a.description=request.POST.get('des')
        a.save()
        return redirect(productdisplay)
    return render(request,'edit_product.html',{'i':im,'j':nm,'k':pr,'l':de})

def cart(request,id,iid):
    a=productmodel.objects.get(id=id)
    c=usermodel.objects.get(id=iid)
    b=cartmodel(cartname=a.pname,pid=a.pid,cid=c.id,cartprice=a.price,cartdescription=a.description,cartimage=a.image)
    b.save()
    return redirect(f'/user_profile/{c}/{iid}')



def cartdisplay(request,iid):
    a=cartmodel.objects.all()
    aa=usermodel.objects.get(id=iid)
    x=aa.username
    li=[]
    nm=[]
    pr=[]
    des=[]
    id=[]
    cid=[]
    for i in a:
        f = i.cid
        if iid == f:
            cid.append(f)
            a=i.cartimage
            li.append(str(a).split('/')[-1])
            b=i.cartname
            nm.append(b)
            c=i.cartprice
            pr.append(c)
            d=i.cartdescription
            des.append(d)
            e=i.id
            id.append(e)
    mylist=zip(li,nm,pr,des,id,cid)
    return render(request, 'cart_display.html', {'mylist': mylist,'x':x,'y':iid})


def cartdelete(request,id,iid):
    a=cartmodel.objects.get(id=id)
    a.delete()
    # return HttpResponse('success')
    return redirect(cartdisplay,f'{iid}')


def buy(request,id):
    a=cartmodel.objects.get(id=id)
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price=request.POST.get('price')
        item_quantity = request.POST.get('quantity')
        total=int(item_price)*int(item_quantity)
        return render(request,'finalbill.html',{'a':item_name,'b':item_quantity,'c':total,'d':item_price})
    pr=a.cartprice
    nm=a.cartname
    ii=a.id
    return render(request,'buy.html',{'x':pr,'y':nm,'z':ii})


def nav(request):
    return render(request,'navbar.html')

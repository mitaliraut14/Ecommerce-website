from django.shortcuts import render,redirect
from .models import *
from .models import User
# from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def index(request):
    p=Product.objects.all()
    content={}
    content['data']=p
    return render(request,'index.html',content)

def dashboard(request):
    p=Product.objects.all()
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

def view_product(request,rid):
    p=Product.objects.filter(id=rid)
    content={}
    content['data']=p
    return render(request,'view_product.html',content)

def add_product(request):
    if request.method=="POST":
        shape=request.POST['shape']
        size=request.POST['size']
        location=request.POST['loc']
        price=request.POST['price']
        image=request.POST['img']
        pname=request.POST['pname']
        p=Product.objects.create(shape=shape, size=size, location=location, price=price, image=image, pname=pname)
        p.save()
    return render(request,'add_product.html')

def delete(request,rid):
    p=Product.objects.get(id=rid)#select * from blogapp_post where id=rid
    p.delete()
    return redirect('/udash')

def register(request):
    if request.method=="POST":
        name=request.POST['uname']
        email=request.POST['uemail']
        age=request.POST['age']
        address=request.POST['add']
        upass=request.POST['upass']
        cupass=request.POST['cupass']
        error={}
        err=0
        success={}
        #blank field validation start
        if name=="":
            err=1
            error['errnamemsg']="Name field cannot be Blank"
        elif email=="":
            err=1
            error['erremailmsg']="Username field cannot be Blank"
        elif age=="":
            err=1
            error['erragemsg']="Age field cannot be Blank"
        elif address=="":
            err=1
            error['erraddmsg']="Address field cannot be Blank"
        elif upass=="":
            err=1
            error['errpassmsg']="Password field cannot be Blank"
        elif cupass=="":
            err=1
            error['errcupassmsg']="Confirm Password field cannot be Blank"
        elif upass != cupass:
            err=1
            error['errmismatch']="Password and confirm password didn't matched"
        #field validation end

        if err==0:
            # u=User(username=email,password=upass,first_name=name,is_active=1)
            u=User.objects.create(username=email,password=upass,name=name,age=age, address=address)
            print(u)
            u.save()
            success['msg']="User Created Successfully!"
            return render(request,'login.html',success)
          
        else:
            return render(request,'register.html',error)
    
    else:
            return render(request,'register.html')


def user_login(request):
    if request.method=="POST":
        userid=request.user.id
        email=request.POST['email']
        upass=request.POST['upass']
        usuccess={}
        user =User.objects.values().filter(username=email)
        
        # for user in userList:
        uname=user[0]['username']
        uupass=user[0]['password']
        print(user[0]['username'])
        print(user[0]['password'])
        # request.session['user_id'] = email
        if user is not None:
            # login(request,u)
            if uname==email and uupass==upass:

                return redirect('/')
            else:
                usuccess['umsg']="username or password is worng!"
                return render(request,'login.html',usuccess)    
        else:
            usuccess['umsg']="User Not Registered!"
            return render(request,'login.html',usuccess)    

    else:



        return render(request,'login.html')




def setsession(request):
    request.session['email']="admin@gmail.com"
    request.session['upass']="admin123"
    return render(request,'setsession.html')

def getsession(request):
    data={}
    data['semail']=request.session['email']
    data['pass']=request.session['upass']
    return render(request,'getsession.html',data)
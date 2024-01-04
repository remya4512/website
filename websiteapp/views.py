from django.shortcuts import redirect,render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'home.html')
def loginpage(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')

@login_required(login_url='loginpage')
def about(request):
    # if 'uid' in request.session:
    # if request.user.is_authenticated:
        return render(request,'about.html')
    # else:
    #     return render(request,'login.html')

def adduser(request):
    if request.method=='POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        email =request.POST['email']
        password=request.POST['password']
        cpassword =request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
               messages.info(request,'This username already exists....')
               return redirect('signup')
            else:
                user=User.objects.create_user(
                   first_name=first_name,
                   last_name=last_name,
                   username=username,
                   email=email,
                   password=password )
                user.save()
        else:
            messages.info(request,'Password does not match....')
            return redirect('signup')
        
        return redirect('loginpage')

    return render(request,'signup.html')

def login1(request):
    if request.method=='POST':
        username =request.POST['username']
        password =request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            # request.session['uid']=user.id
            auth.login(request,user)
            messages.info(request,f'Welcome {username}')
            return redirect('about')
        else:
            messages.info(request,'Invalid username or password...Try again')
            return redirect('loginpage')
        
    else:
            
            return redirect('loginpage')    

@login_required(login_url='loginpage')
def logout(request):
    # request.session['uid']=''
    # if request.user.is_authenticated:
        auth.logout(request)
        return redirect('home') 



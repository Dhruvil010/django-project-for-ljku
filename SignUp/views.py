from django.shortcuts import render,redirect
from django.http import HttpResponse
from SignUp.forms import SignUpForm  
from SignUp.models import SignUp  

# Create your views here.

def signup(request):
    return render(request,'SignUp.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'SignUp.html')

def sup(request):  
   
    if request.method == "POST": 
        
        form = SignUpForm(request.POST or None) 
        # form.save() 
        # return HttpResponse(form.is_valid())  
        
        if form.is_valid():
            
            try:  
                print("Hello")
                form.save()  
                return render(request,'login.html')  
            except:  
                pass  
    else:  
        form = SignUpForm()  
    return render(request,'SignUp.html',{'form':form})

def loginHandle(request):
    
    if request.method == "POST":    
        form = SignUpForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        uname = SignUp.objects.all().filter(username=un)
        
       
        if uname[0].username == un and uname[0].password == ps:
            return render(request,'home.html')  
            # return HttpResponse('successful')
       
    else:
        form = SignUpForm()
        return render(request, template_name = "login.html", context = {"form":form})
  

from django.shortcuts import render,redirect
from .forms import MyRegistraterForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import RegistrationForm
# Create your views here.
def home(request):
    data=RegistrationForm.objects.all()
    if(data!=''):
        return render(request,'home.html',{'data':data})
    else:
      return render(request ,'home.html')

@csrf_exempt
def insert(request):
    if request.method=='POST':
        form = MyRegistraterForm(request.POST)#get the data from form using post method
        if form.is_valid():
            try:
                form.save()#save the data in form
                messages.success(request,"Registration Successfully completed")
                return redirect("Home")
            except:
                pass
    else:
       form=MyRegistraterForm()
       page ={
        "forms":form,
        
       }
    return render(request, 'register.html',page)
@csrf_exempt
def update(request,id):
    datas=RegistrationForm.objects.get(id=id)
    if request.method=="POST":
       name=request.POST['name']
       age=request.POST['age']
       address=request.POST['address']
       contact=request.POST['contact']
       email=request.POST['email']
        
       datas.name=name
       datas.age=age
       datas.address=address
       datas.contact=contact
       datas.email=email
       datas.save()
       messages.success(request,"updated successfully")
       return redirect('Home')
    else:
        return render(request, 'update.html',{'data':datas})
    
def delete(request,id):
    data=RegistrationForm.objects.get(id=id)
    data.delete()
    messages.success(request,"Delete successfully")
    return redirect("Home")
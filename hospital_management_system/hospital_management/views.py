from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .forms import BookingForm, ContactForm
from .models import Departments,Doctors
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.



def index(request):
    return render(request, "index.html")

def about(request):
    return render(request,"about.html")

def booking(request):

    if request.method =="POST":
        form= BookingForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request,'confirmation.html')
    form = BookingForm()

    dict_form={
        'form':form
    }
    return render(request,"booking.html",dict_form)
    

def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,"department.html",dict_dept)
   
def doctors(request):
    doc_dict={
        'doc':Doctors.objects.all()
    }
    return render(request,"doctors.html",doc_dict)
   
def contact(request):
    if request.method=='POST':
        
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contactconfirm.html')
        # name= request.POST.get('name')
        # email=request.POST.get('email')
        # message=request.POST.get('message')
    form =ContactForm()
    
    dict_forms={
        'form':form
    }
        

    return render(request,"contact.html", dict_forms)


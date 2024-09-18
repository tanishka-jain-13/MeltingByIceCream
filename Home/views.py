from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages


# Create your views here.

# URL dispatcherssss , it take functions to urlspy home

def index(request):
    #context is set of variables. which are sended.
    context = {
        "variable" : "this is sent. "
    }
    
    return render(request, 'index.html', context)
    #return HttpResponse(" This is homepage. ")

# about page

def about(request):
    context = {
        'title': 'About Us',
    }
    return render(request, 'about.html', context)
    #return HttpResponse(" This is about page. ")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse(" This is services page. ")

def icecream(request):
    return render(request, 'icecream.html')

def softy(request):
    return render(request, 'softy.html')

def familypack(request):
    return render(request, 'familypack.html')

#contact page
 
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone= phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    
    return render(request, 'contact.html')
   # return HttpResponse(" This is contact page. ")

from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.


def index(request):
    context = {'variable': 'maaza hi mazaa'}
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')

# Learning database now
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        # date = datetime.today()
        contactsave = Contact(name = name, email = email, phone = phone)
        contactsave.save()
        message = {'sent' : 'message'}
        # message.sucess(request, 'Your message has been sent')
    return render(request, 'contact.html', message)


 


from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact

# Create your views here.


def home(request):
    context = {'name': 'harry', 'course': 'django'}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.ge('phone')
        desc = request.POST.get('desc', False)
        # print(name, email, phone, desc)
        contact= Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        print("the data has been return to the db")

    return render(request, 'contact.html')

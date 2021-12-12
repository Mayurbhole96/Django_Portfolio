from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
   # context = {'name': 'Mayur', 'course': 'Django'}
    context = {'name': 'Nandu', 'course': 'Python'}
    return render(request, 'home.html', context)

def about(request):
   # return HttpResponse("This is My about Page (/about)")
    return render(request, 'about.html')

def project(request):
   # return HttpResponse("This is My project Page (/project)")
    return render(request, 'project.html')
    
def contact(request):
   if request.method=="POST":
      name = request.POST['name']
      email = request.POST['email']
      phone = request.POST['phone']
      cmt = request.POST['cmt']
      #print(name, email, phone, cmt)
      contact = Contact(name=name, email=email, phone=phone, cmt=cmt)
      contact.save()
      print("The data has been written to the db")
     # context = {'success': True }

    # return HttpResponse("This is My contect Page (/contect)")   
             
   return render(request, 'contact.html')

def desable(request):
    return render(request, 'desable.html')   
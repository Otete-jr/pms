from django.shortcuts import render

#home page
def home(request):
    return render(request,'home.html')
#application
def application(request):
    return render(request,'application.html')
#admin
def login(request):
    return render(request,'login.html')


from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    name = 'Toey'
    age = 26
    return render(request, "index.html", {'name':name,"age":age})

def about(request):
    return render(request, "about.html")

def form(request):
    return render(request, "form.html")

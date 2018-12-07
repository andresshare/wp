from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"kernel/home.html",{})

def about(request):
    return render(request,"kernel/about.html",{})



def contacto(request):
    return render(request,"kernel/contacto.html",{})

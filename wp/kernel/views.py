from django.shortcuts import render, HttpResponse

barra_nav = """
 <h1>WP</h1>
 <ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/">About</a></li>
    <li><a href="/">Portfolio</a></li>
    <li><a href="/">Contacto</a></li>
 </ul>
"""

def home(request):
    return render(request,"kernel/home.html",{})

def about(request):
    return HttpResponse(barra_nav + "<h2>About</h2>")

def portfolio(request):
    return HttpResponse(barra_nav + "<h2>Portfolio</h2>")

def contacto(request):
    return HttpResponse(barra_nav + "<h2>Contacto</h2>")

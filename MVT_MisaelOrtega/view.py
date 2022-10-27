from django.http import HttpResponse
from django.shortcuts import render



def aboutme(request):
    data = {'name': 'Julia', 'age': '28', 'zodiac':'piscis'}
    return render (request, "acerca.html", data)

def inicio(request):
    return render (request, "inicio.html")



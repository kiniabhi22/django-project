from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello</h1>")
def menu(request):
    return render(request,'index.html')
def back(request):
    return HttpResponse("To move to back<a href='/'>click</a>")
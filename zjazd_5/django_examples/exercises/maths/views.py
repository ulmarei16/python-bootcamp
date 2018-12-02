from django.shortcuts import render
from django.http import HttpResponse, response
# Create your views here.
def math_operations(request, name, param1, param2):
    if name == "add":
        wynik = int(param1) + int(param2)
    elif name == "sub":
        wynik = int(param1) - int(param2)
    elif name == "mul":
        wynik = int(param1) * int(param2)
    return HttpResponse(content=f"Wynik: {wynik}")

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, response

def main_page(request):
    return HttpResponse(content="To jest main page.")

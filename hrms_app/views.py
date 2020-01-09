from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def index(request):
  return HttpResponse("Hello men!")

def show(request, id):
  p = Person.objects.get(id)
  return HttpResponse("person")
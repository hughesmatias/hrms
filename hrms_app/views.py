from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Person
from django.template import loader
from django.core import serializers

# Create your views here.
def index(request):
  return HttpResponse("Hello men!")

def show(request, id):
  template = loader.get_template("person/index.html")
  try:
    p = Person.objects.get(id=id)
  except Person.DoesNotExist:
    raise Http404("Person does not exist")
  return HttpResponse(template.render({
    'lastName': p.lastName,
    'firstName': p.firstName
  }, request))

  
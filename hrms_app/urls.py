# URLConf

from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("person/<int:id>", views.getBiyId),
  path("person/<int:id>/show", views.show, name="show")
]
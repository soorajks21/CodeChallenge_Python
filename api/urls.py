from django.urls import path
from api import views

urlpatterns=[path("ribo/",views.RandomAPI.as_view())]
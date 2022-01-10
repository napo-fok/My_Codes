from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello Django</h1>')

def about(request):
    return HttpResponse('<h1>A Propos</h1> <p>Cette Application est Magnifique</p>')

def listing(request):
    return HttpResponse('<h1>Listings</h1> <p>Page pour les Listings</p>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1> <p>Notre Adresse et Contact téléphonique</p>')

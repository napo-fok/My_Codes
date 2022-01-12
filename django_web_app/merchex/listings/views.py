from typing import List
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands':bands})

def about(request):
    return render(request,'listings/about.html')

def listing(request):
    lis=Listing.objects.all()
    return render(request,'listings/listings.html', {'titles':lis})

def contact(request):
    return render(request,'listings/contact.html')

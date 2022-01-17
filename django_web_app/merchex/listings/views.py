from typing import List
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands':bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band':band})

def about(request):
    return render(request,'listings/about.html')

def listing_list(request):
    lists=Listing.objects.all()
    return render(request,'listings/listing_list.html', {'lists':lists})

def listing_list_group(request, band_id): # In creation
    band=Band.objects.get(id=band_id)
    return render(request,'listings/listing_list_group.html', {'band':band})

def listing_detail(request, listing_id):
    lis=Listing.objects.get(id=listing_id)
    return render(request,'listings/listing_detail.html', {'lis':lis})

def contact(request):

    print("La méthode de requête est: ", request.method)
    print("Les données POST sont: ", request.POST)

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],)

            return redirect('email_sent')
        
        # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
        # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    
    return render(request,'listings/contact.html', {'form':form})

def contact_email_sent(request):
    return render(request,'listings/email_sent.html')

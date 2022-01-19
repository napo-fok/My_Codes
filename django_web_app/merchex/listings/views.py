from typing import List
from django.http import HttpResponse
from django.shortcuts import render
from listings.forms import ListingForm
from listings.forms import BandForm
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands':bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html', {'band':band})

def band_create(request):
    print("La méthode de requête est : ", request.method)
    print("Les données POST sont : ", request.POST)

    if(request.method == 'POST'):
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()

            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request, 'listings/band_create.html', {'form':form})

def band_update(request, band_id):
    band = Band.objects.get(id=band_id)
    
    print("La méthode de requête est : ", request.method)
    print("Les données POST sont : ", request.POST)

    if(request.method == 'POST'):
        form = BandForm(request.POST, instance=band) #Le mot clé 'Instance' permet de pré-remplir le formulaire
        if form.is_valid():
            band = form.save()

            return redirect('band-detail', band.id)

    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html', {'form':form})

def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    messages.add_message(request, messages.INFO, 'Le groupe {0} a été supprimé.'.format(band.name))
    print("La méthode de requête est : ", request.method)
    print("Les données POST sont : ", request.POST)

    if(request.method == 'POST'):

        band.delete()
        return redirect('band-list')

    return render(request, 'listings/band_delete.html', {'band':band})

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

def listing_create(request):
    print("La méthode de requête est : ", request.method)
    print("Les données POST sont : ", request.POST)

    if(request.method == 'POST'):
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()

            return redirect('listing-detail', listing.id)

    else:
        form = ListingForm()

    return render(request, 'listings/listing_create.html', {'form':form})

def listing_update(request, listing_id):
    lis = Listing.objects.get(id=listing_id)

    print("La méthode de requête est : ", request.method)
    print("Les données POST sont : ", request.POST)

    if(request.method == 'POST'):
        form = ListingForm(request.POST, instance=lis)
        if form.is_valid():
            listing_ret = form.save()

            return redirect('listing-detail', listing_ret.id)

    else:
        form = ListingForm(instance=lis)

    return render(request, 'listings/listing_update.html', {'form':form})

def listing_delete(request, listing_id):
    lis = Listing.objects.get(id=listing_id)
    messages.add_message(request, messages.INFO, 'L\'annonce {0} a été supprimée.'.format(lis.title))
    print("La méthode de requête est : ", request.method)
    print("Les données POST sont : ", request.POST)

    if(request.method == 'POST'):
        lis.delete()
        return redirect('listing-list')

    return render(request, 'listings/listing_delete.html', {'lis':lis})


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

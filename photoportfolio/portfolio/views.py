from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def home(request):
    return render(request, 'portfolio/home.html')

def gallery(request):
    return render(request, 'portfolio/gallery.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('idea')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})


def idea(request):
    contacts = Contact.objects.all()
    return render(request, 'portfolio/idea.html', {'contacts': contacts})
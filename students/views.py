from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'navbar':'index'})

def about(request):
    return render(request, 'about.html', {'navbar':'about'})

def classes(request):
    return render(request, 'classes.html', {'navbar': 'classes'})
def contacts(request):
    return render(request, 'contacts.html', {'navbar': 'contacts'})

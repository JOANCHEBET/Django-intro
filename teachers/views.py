from django.shortcuts import render

# Create your views here.
def about(request):
    context={'navbar=index'}
    return render(request, 'about.html',context)
def classes(request):
    return render(request, 'classes.html')
def contacts(request):
    return render(request,'contacts.html')

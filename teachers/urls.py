
from django.urls import path
from . import views
app_name='teachers'

urlpatterns = [

    path('about/', views.about, name='about'),
    path('classes/', views.classes,name='classes'),
    path('contacts/', views.contacts, name='contacts')
]
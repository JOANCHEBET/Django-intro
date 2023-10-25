
from django.urls import path
from . import views
app_name="students"
urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('classes/', views.classes, name='classes'),
    path('contacts/', views.contacts, name='contacts')

]
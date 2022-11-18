from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
import random

def index(request):
    return render(request, 'generador/index.html')

def about(request):
    return render(request,'generador/about.html')

def password(request):
    
    """ Obtiene la solicitud que manda el usuario """
    length =request.GET.get('length')
    
    
    """ Ibten una serie de acaracteres aleatorio """
    characters =list('abcdefghijklmnopqrstuwxyz1234567890!@#$%^&*()_+-')
    generated_password = ''
    for char in range(10):
        generated_password+= random.choice(characters)
    
    
    return render(request,'generador/password.html', {'password':generated_password } )
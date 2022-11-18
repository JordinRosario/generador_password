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
    length =int(request.GET.get('soli'))


    """ Ibten una serie de acaracteres aleatorio """
    characters =list('abcdefghijklmnopqrstuwxyz')
    generated_password = ''
    for char in range(length):
        generated_password+= random.choice(characters)
    
    
    return render(request,'generador/password.html', {'password':generated_password } )
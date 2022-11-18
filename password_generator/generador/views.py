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
    
    Caracteres =list('abcdefghijklmnopqrstuwxyz')
    if request.GET.get('uppercase'): #Comprueba si quiere la contraseña con letras MUYUS
        Caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUWXYZ'))
        
    if request.GET.get('number'): #Comprueba si quiere que la contraseña contenga numeros
        Caracteres.extend(list('1,2,3,4,5,6,7,8,9,0'))
        
    if request.GET.get('simbolos'):
        Caracteres.extend(list('~`!@#$%^&*()_+-=/\;:?><.,'))
    
    """ Ibten una serie de acaracteres aleatorio """
    generated_password = ''
    for char in range(length):
        generated_password+= random.choice(Caracteres)
    
    
    return render(request,'generador/password.html', {'password':generated_password } )
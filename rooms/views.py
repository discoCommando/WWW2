from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

def main(request):
    return render(request, 'main.html')

#def lista(request):
    #pozycje = Pozycja.objects.all()
    #slownik = {'poz': pozycje}
    #return render(request, 'lista.html', slownik)

#def lista_zalogowana(request):
    #if request.user.is_authenticated():
        #return lista(request)
    #else:
        #return redirect('glowna')

def logout_(request):
    logout(request)
    return redirect('main')

def login_(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            messages.error(request, 'Konto zablokowane')
    else:
        messages.error(request, 'Zle haslo')
    return redirect('main')

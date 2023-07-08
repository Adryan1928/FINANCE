from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Conta


# Create your views here.


def home (request):
    return render(request, 'home.html')

def gerenciar (request):
    return render(request, 'gerenciar.html')

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    conta = Conta(
        apelido=apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone)
    
    conta.save()
    return redirect('/perfil/gerenciar/')
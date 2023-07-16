from django.shortcuts import render, redirect
from perfil.models import Categoria
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.

def definir_planejamento(request):
    categorias = Categoria.objects.all()

    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor = json.load(request)['novo_valor']
    novo_valor = novo_valor.replace(',', '.')
    
    categoria = Categoria.objects.get(id = id)
    categoria.valor_planejamento = float(novo_valor)

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Valor atualizado')

    return redirect('/planejamento/definir_planejamento/')

def ver_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'ver_planejamento.html', {'categorias': categorias})

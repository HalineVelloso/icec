from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import context

from .forms import ProdutoForm, CompraForm
from .models import Produto, Compra
# Create your views here.
def index(request):
    return render(request, 'index.html')

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                messages.success(request, 'Produto salvo com sucesso.')
            else:
                messages.error(request, 'Erro ao salvar o produto.')
        else:
            form = ProdutoForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')

def compra(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = CompraForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Compra salva com sucesso.')
            else:
                messages.error(request, 'Erro ao salvar a compra.')
        else:
            form = CompraForm()
        context = {
            'form': form
        }
        return render(request, 'compra.html', context)
    else:
        return redirect('index')

def estoque(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'estoque.html', context)

def comprasrealizadas(request):
    context = {
        'compras': Compra.objects.all()
    }
    return render(request, 'comprasrealizadas.html', context)

def cadastro(request):
    return render(request, 'cadastro.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ProdutoFilter
from django.http import HttpResponse
from django.template import loader

from .forms import ProdutoForm, CompraForm, RetiradaForm, CustomUsuarioCreateForm
from .models import Produto, Compra, Retirada
# Create your views here.
def index(request):
    return render(request, 'index.html')

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = ProdutoForm()
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
                form = CompraForm()
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

def retirada(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = RetiradaForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    form.save()
                    form = RetiradaForm()
                    messages.success(request, 'Retirada realizada com sucesso.')
                except Exception as e:
                    messages.error(request, e)
        else:
            form = RetiradaForm()
        context = {
            'form': form
        }
        return render(request, 'retirada.html', context)
    else:
        return redirect('index')

def estoque(request):
    produto_list = Produto.objects.all().order_by('nome', 'categoria')
    produto_filter = ProdutoFilter(request.GET, queryset=produto_list)
    
    paginator = Paginator(produto_filter.qs, 10)
    page = request.GET.get('page')

    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        produtos = paginator.page(1)
 
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)
    
    return render(request, 'estoque.html', {'page':page,'produtos':produtos, 'produto_filter': produto_filter})
    

def comprasrealizadas(request):
    comprasrealizadas_list = Compra.objects.all().order_by('-id')
    paginator = Paginator(comprasrealizadas_list, 10)
    page = request.GET.get('page')
 
    try:
        compras = paginator.page(page)
    except PageNotAnInteger:
        compras = paginator.page(1)
 
    except EmptyPage:
        compras = paginator.page(paginator.num_pages)
    return render(request, 'comprasrealizadas.html', {'page':page,'compras':compras})

def cadastro(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = CustomUsuarioCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = CustomUsuarioCreateForm()
                messages.success(request, 'Cadastro realizado com sucesso.')
            else:
                messages.error(request, 'Erro ao realizar cadastro.')
        else:
            form = CustomUsuarioCreateForm()
        context = {
            'form': form
        }
        return render(request, 'cadastro.html', context)
    else:
        return redirect('index')

def retiradasrealizadas(request):
    retiradasrealizadas_list = Retirada.objects.all().order_by('-id')
    paginator = Paginator(retiradasrealizadas_list, 10)
    page = request.GET.get('page')
 
    try:
        retiradas = paginator.page(page)
    except PageNotAnInteger:
        retiradas = paginator.page(1)
 
    except EmptyPage:
        retiradas = paginator.page(paginator.num_pages)
    return render(request, 'retiradasrealizadas.html', {'page':page,'retiradas':retiradas})

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return  HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
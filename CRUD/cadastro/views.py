from django.shortcuts import render, redirect
from .models import Pessoa
from .form import PessoaForm

def home(request):
    data = {}
    data['pessoa'] = Pessoa.objects.all()
    return render(request, 'cadastro/home.html', data)

def novo_cadastro(request):
    data = {}
    form = PessoaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_home')

    data['form'] = form
    return render(request, 'cadastro/form.html', data)

def update(request, pk):
    data = {}
    pessoa = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('url_home')

    data['form'] = form
    data['pessoa'] = pessoa
    return render(request, 'cadastro/form.html', data)

def delete(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    pessoa.delete()
    return redirect('url_home')

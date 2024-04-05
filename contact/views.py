from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request,
        'contact/index.html',
    )
    
def lançamento(request):
    return render(
        request,
        'contact/lançamento.html'
    )
    
def programaçaoDeHoje(request):
    return render(
        request,
        'contact/programaçaoDeHoje.html'
    )
    
def series(request):
    return render(
        request,
        'contact/series.html'
    )
    
def filmes(request):
    return render(
        request,
        'contact/filmes.html'
    )
 
    
def contato(request):
    return render(
        request,
        'contact/contato.html'
    )
       

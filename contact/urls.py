
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('lançamento/', views.lançamento, name= 'lançamento'),
    path('programaçaoDeHoje/', views.programaçaoDeHoje, name= 'programaçaoDeHoje'),
    path('series/', views.series, name= 'series'),
    path('filmes/', views.filmes, name= 'filmes'),
    path('contato/', views.contato , name= 'contato'),
   

    
]

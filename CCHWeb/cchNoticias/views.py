from django.shortcuts import render, redirect
from .models import Noticias,Comentario
from .forms import NoticiasForms

# Create your views here.


def home(request):
    noticias = Noticias.objects.all()
    return render(request, 'home.html', {'noticias': noticias})

def noticias(request, id):
    noticia = Noticias.objects.get(id = id)
    comentarios = Comentario.objects.all().filter(blog=id)
    form = NoticiasForms(request.POST or None)
    
    if form.is_valid():
        comentario = form.save(commit=False)
        print("Mensagem:", comentario)
        comentario.blog_id = noticia.id
        comentario.save()
        return redirect('home')

    return render(request, 'noticias.html', { 'noticia': noticia, 'form':form, 'comentarios':comentarios})

# Create your views here.
from django.shortcuts import render, redirect

from purple.models import Libro, Recomendado


def index(request):
    lista_libros = Libro.objects.all()
    lista_recomendado = Recomendado.objects.all()
    return render(request, 'purple/index.html', {'recomendados': lista_recomendado, 'libros': lista_libros})



def crear_libro(request):

    #GET -> devolver al usuario  el html vacio de crear libro
    if request.method == 'GET':
        return render(request, index)
    #POST-> crear el libro en la BBDD y devolvernos a la pantalla de inicio
    else:
        libro_nuevo = Libro()
        libro_nuevo.id = request.POST.get('id')
        libro_nuevo.img = request.POST.get('img')
        libro_nuevo.nombre = request.POST.get('nombre')
        libro_nuevo.autor = request.POST.get('autor')
        libro_nuevo.fecha_publicacion = request.POST.get('fecha')

        Libro.save(libro_nuevo)

        return redirect(index)


def crear_recomendado(request):

    #GET -> devolver al usuario  el html vacio de crear libro
    if request.method == 'GET':
        return render(request, index)
    #POST-> crear el libro en la BBDD y devolvernos a la pantalla de inicio
    else:
        libro_nuevo = Recomendado()
        libro_nuevo.id = request.POST.get('id')
        libro_nuevo.img = request.POST.get('img')
        libro_nuevo.nombre = request.POST.get('nombre')
        libro_nuevo.autor = request.POST.get('autor')
        libro_nuevo.fecha_publicacion = request.POST.get('fecha')

        Libro.save(libro_nuevo)

        return redirect(index)


def editar_libro(request):
    if request.method == 'GET':
        libro = Libro.objects.get(id=id)
        return render(request, 'purple/edit.html', {'libro': libro})

    else:
        libro_nuevo = Libro()
        libro_nuevo.id = request.POST.get('id')
        libro_nuevo.img = request.POST.get('img')
        libro_nuevo.nombre = request.POST.get('nombre')
        libro_nuevo.autor = request.POST.get('autor')
        libro_nuevo.fecha_publicacion = request.POST.get('fecha')

        Libro.save(libro_nuevo)

        return redirect(index)

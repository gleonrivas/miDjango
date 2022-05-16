from django.urls import path


from .views import *

urlpatterns = [
    path('', index),
    path('crear', crear_libro),
    path('edit_book/<int:id>', editar_libro, name='editar_libro'),
    path('delete_book/<int:id>', borrar_libro, name='borrar_libro')
]

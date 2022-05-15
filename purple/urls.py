from django.urls import path


from .views import *

urlpatterns = [
    path('', index),
    path('crear', crear_libro),
    path('edit_book/<int:id>', editar_libro, name='editar'),
    path('editar', editar_libro),
]

from django.urls import path
from . import views, class_view

urlpatterns = [
    path('',views.inicio, name='index'),
    path('crear/',views.crearPersona, name='crear_persona'),
    path('editar/<int:id>/',views.editarPersona, name='editar_persona'),
    path('eliminar/<int:id>/',views.eliminarPersona, name='eliminar_persona'),
    path('listclass/', class_view.PersonaList.as_view(), name='list_persona' ),
    path('create/', class_view.PersonaCreate.as_view(), name='create_persona' ),
    path('update/<int:pk>', class_view.PersonaUpdate.as_view(), name='update_persona' ),
    path('delete/<int:pk>', class_view.PersonaDelete.as_view(), name='delete_persona' ),

]   
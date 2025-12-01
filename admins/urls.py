from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin_index'),
    path('<int:edad>/saludo/<str:nombre>', views.saludo, name='admins_saludo'),
    path('nuevapersona', views.nueva_persona, name='nueva_persona'),
    path('detalle/<int:id>', views.detalle, name='detalle_persona'),
    path('editar/<int:id>', views.editar_persona, name="editar_persona"),
]


# localhost:8000/admins/30/saludo/Juan
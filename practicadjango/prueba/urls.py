from django.urls import path

from prueba import views

urlpatterns = [
    path('test', views.holamundo, name='holamundo'),
    path('personas/create', views.personas_create, name="personas_create"),
    path('personas/<int:persona_id>/delete', views.personas_delete, name="personsas_delete"),
    path('personas/<int:persona_id>', views.personas_update, name="personas_update"),
    # path('personas/<int:persona_id>', views.detalle_persona, name="detalle"),
    path('personas', views.personas_list, name="personas_list")
]

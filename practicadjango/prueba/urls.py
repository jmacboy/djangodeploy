from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from prueba import views
from prueba.api import PersonaViewSet

router = routers.DefaultRouter()
router.register(r'personas-api', PersonaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('test', views.holamundo, name='holamundo'),
    path('personas/create', views.personas_create, name="personas_create"),
    path('personas/<int:persona_id>/delete', views.personas_delete, name="personsas_delete"),
    path('personas/<int:persona_id>', views.personas_update, name="personas_update"),
    # path('personas/<int:persona_id>', views.detalle_persona, name="detalle"),
    path('personas', views.personas_list, name="personas_list")
]

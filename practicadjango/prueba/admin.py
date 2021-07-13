from django.contrib import admin

# Register your models here.
from prueba.models import Persona


class PersonaAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "ciudad", "genero")
    list_filter = ["genero", "ciudad"]


admin.site.register(Persona, PersonaAdmin)

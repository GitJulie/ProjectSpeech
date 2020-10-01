from django.contrib import admin

from .models import Language, Website, Auteur

admin.site.register(Language)
admin.site.register(Website)
admin.site.register(Auteur)

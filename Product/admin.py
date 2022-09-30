from django.contrib import admin
from .models import Posteo, Contacto

class PosteoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor","fecha"]
    search_fields = ["autor"]
    list_filter = ["autor","fecha"]
    list_per_page = 5


admin.site.register(Posteo,PosteoAdmin)
admin.site.register(Contacto)

# Register your models here.

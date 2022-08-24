from django.urls import path
from Product.views import ver_familiar, crear_familiar

urlpatterns = [
    path('datos/', ver_familiar, name ="familiares"),
    path('crear/<nombre>', crear_familiar)
]
from django.urls import path
from Product.views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', inicio, name ="Inicio"),
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='paginas/logout.html'), name='Logout'),
    path('contactos/', views.contacto, name="Contacto"),
    path('modificar-publicacion/<pk>', views.BlogUpdate.as_view(), name="Update"),
    path('borrarBlog/<pk>', views.BlogDelete.as_view(), name="Delete"),
    path('detalleBlog/<pk>', views.BlogDetail.as_view(), name="Detail"),
    path('about/', views.about, name="About"),
    path(r'^perfil/$', views.perfil, name="Perfil"),
    path('editarPerfil/', views.editarPerfil, name="editarPerfil"),
    path('createBlog/', views.BlogPost.as_view(), name="Create"),
]
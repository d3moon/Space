from django.contrib import admin
from django.urls import path
from galeria.views import index, imagens

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('imagem/', imagens, name='imagem'),
]

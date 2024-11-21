from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contacto/enviar/', enviar_contacto, name='enviar_contacto'),
]

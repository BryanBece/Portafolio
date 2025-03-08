from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.


projects = [
    {
        "name": "InfoCáncer",
        "image": "img/mini/WebPractica.jpg",
        "description": "Proyecto de título. Se trata de una web para recabar información sobre el cáncer de mama a través de un bot de WhatsApp y generar informes en la web.",
        "github_url": "https://github.com/BryanBece/PortafolioTitulo",
        "demo_url": "https://infocancerchile.pythonanywhere.com/",
        "tools": ["Django", "HTML", "CSS", "JavaScript", "SQL", "Bootstrap", "Python"]
    },
    {
        "name": "Dashboard",
        "image": "img/mini/Dashboard.jpg",
        "description": "Proyecto estudiantil. Se trata de una maquetación de un dashboard para gestión de inventarios con distintos roles.",
        "github_url": "https://github.com/BryanBece/inventoryCrud",
        "demo_url": "https://bryanbece.github.io/inventoryCrud/",
        "tools": ["HTML", "CSS", "JavaScript"]
    },
    {
        "name": "PokeWeb",
        "image": "img/mini/PokeWeb.jpg",
        "description": "Proyecto realizado con la PokeApi. Se trata de una web que muestra información de los Pokémon.",
        "github_url": "https://github.com/BryanBece/PokeWeb",
        "demo_url": "https://portfoliobryanbece.pythonanywhere.com/pokeWeb/",
        "tools": ["Django", "HTML", "CSS", "JavaScript", "Bootstrap"]
    },
    {
        "name": "El Comilón",
        "image": "img/mini/ElComilon.jpg",
        "description": "Proyecto estudiantil. Se trata de una web para un local de comida rápida.",
        "github_url": "https://github.com/BryanBece/ElComilon",
        "demo_url": "https://elcomilonweb.pythonanywhere.com/",
        "tools": ["Django", "HTML", "CSS", "JavaScript", "SQL"]
    }
]


def home(request):
    return render(request, 'webCore/index.html', {"projects": projects})

def enviar_contacto(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        
        # Aquí se envía el mensaje por correo
        send_mail(
            f'Mensaje de {nombre} ({email})',
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            ['destinatario@example.com'],  # Cambia este correo por el que quieres recibir los mensajes
            fail_silently=False,
        )
        return HttpResponse('Mensaje enviado con éxito!')
    
    return HttpResponse('Método no permitido', status=405)

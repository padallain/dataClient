from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Client
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a la aplicación Sample Mflix</h1>")


@csrf_exempt
def create_client(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parsear el cuerpo de la solicitud como JSON
            print(data)  # Imprimir los datos recibidos para depuración
            client = Client.objects.create(
                id=data['id'],  # Acepta el ID proporcionado en la solicitud
                nombre=data['nombre'],
                latitude=data['latitude'],
                longitude=data['longitude'],
                start=data['start'],
                end=data['end']
            )
            return JsonResponse({'message': 'Cliente creado exitosamente', 'id': client.id}, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Falta el campo requerido: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
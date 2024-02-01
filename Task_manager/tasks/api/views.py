from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks.models import Task
from .serializers import TaskSerializer

# def getRoutes(request):
#     routes = [
#         'GET /api',
#         'GET /api/task',
#         'GET /api/task/:id'
#     ]
#     return JsonResponse(routes,safe=False)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/task',
        'GET /api/task/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)    
    return Response(serializer.data)

@api_view(['GET'])
def getTask(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks,many=False)    
    return Response(serializer.data)
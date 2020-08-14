from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from ..models import QiyaoEvent
from .serializers import EventSerializer


@csrf_exempt
def event_list(request):
    if request.method == "GET":
        events = QiyaoEvent.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def event_detail(request, pk):
    try:
        event = QiyaoEvent.objects.get(pk=pk)
    except QiyaoEvent.DoesNotExist:
        return JsonResponse({"Error": "Event(pk={}) not found".format(pk)}, status=404)
    if request.method == "GET":
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = EventSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        event.delete()
        return HttpResponse(status=204)

from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Event, ParkingLot, ParkingSpot
from django.http import HttpResponse

# http://127.0.0.1:8000/api/current_events/?num=5
def get_events(request):
    try:
        number = int(request.GET['num'])
        events = Event.objects.order_by('-date')[:number]

        json = serialize("json", events, fields=('name', 'date'))

        return HttpResponse(json, content_type="application/json")
    except:
        response = JsonResponse({"error": "Invalid event list request"})
        response['Access-Control-Allow-Origin'] = '*'
        return response


def get_lots(request):
    pass

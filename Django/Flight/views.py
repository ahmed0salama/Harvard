from django.shortcuts import render
from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flight/index.html", {"flights": Flight.objects.all(), 'lenght': len(Flight.objects.all())})

def flight(request, flight_id):
    f = Flight.objects.get(id=flight_id)
    return render(request, "flight/flight.html", {'flight':f, 'passengers':Passenger.objects.filter(flights=f)})

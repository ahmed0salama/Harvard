from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flight/index.html", {"flights": Flight.objects.all(), 'lenght': len(Flight.objects.all())})

def flight(request, flight_id):
    f = Flight.objects.get(pk=flight_id)
    return render(request, "flight/flight.html", {'flight':f, 
                                                  'passengers':Passenger.objects.filter(flights=f),
                                                  'non_passengers':Passenger.objects.exclude(flights=f).all()
                                                  })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight', args=[flight_id]))

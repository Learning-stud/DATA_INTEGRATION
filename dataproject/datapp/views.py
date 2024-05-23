from django.db.models import Q
from django.shortcuts import render
from .models import Flight

def flight_search(request):
    flights = None
    if request.method == "POST":
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        print(f"Origin: {origin}, Destination: {destination}")  # Debug print
        flights = Flight.objects.filter(Q(origin__icontains=origin) & Q(destination__icontains=destination))
        print("Flights count:", flights.count())  # Debug print
        for flight in flights:
            print(f"Flight: {flight.origin} to {flight.destination}, Sector: {flight.sector}")  # Debug print
    return render(request, 'datapp/index.html', {'flights': flights})

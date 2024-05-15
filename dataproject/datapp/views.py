
# # Create your views here.
# # views.py

# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Flight
# from .forms import FlightSearchForm

# def flight_search(request):
#     if request.method == 'POST':
#         form = FlightSearchForm(request.POST)
#         if form.is_valid():
#             origin = form.cleaned_data['origin']
#             destination = form.cleaned_data['destination']
#             flights = Flight.objects.filter(origin__icontains=origin, destination__icontains=destination)
#             return render(request, 'your_app/flight_result.html', {'flights': flights})
#     else:
#         form = FlightSearchForm()
#     return render(request, 'datapp/flight_search.html', {'form': form})

# def get_city_suggestions(request):
#     term = request.GET.get('term', '')
#     origins = Flight.objects.filter(origin__icontains=term).values_list('origin', flat=True).distinct()
#     destinations = Flight.objects.filter(destination__icontains=term).values_list('destination', flat=True).distinct()
#     suggestions = list(set(origins) | set(destinations))  # Combine and deduplicate
#     return JsonResponse(suggestions, safe=False)
from django.shortcuts import render
from .models import Flight

def flight_search(request):
    flights = None
    if request.method == "POST":
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        flights = Flight.objects.filter(origin=origin, destination=destination)
    return render(request, 'your_app/index.html', {'flights': flights})

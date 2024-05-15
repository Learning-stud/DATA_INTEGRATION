#  DAT INTEGRATION 

# 1ST
## PROJECT DEPENDENCY
### PYTHON / DJANGO / HTML & CSS / REQUEST LIBRARY / RENDER LIBRARY.

# 2ND
## THINGS TO DO 
###  FIRST CREATED DJANGO PROJECT AND THEN AFTER CRETING THE PROJECT CREATED    CRETED TEMPLATES FOLDER IN TEMPLATES FOLDER ADD 2 FILE ONE FILE TO SAVE RESULT AND ANOTHER TO SHOW SEARCH RESULT ,
### THEN CREATED MODELS NAMES OF ORIGIN & DESTINATION , AFTER CREATING MODELS CREATED FORM.PY USING CLASSBASED TO INOUT METHODS
```

# Create your views here.
# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Flight
from .forms import FlightSearchForm

def flight_search(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            flights = Flight.objects.filter(origin__icontains=origin, destination__icontains=destination)
            return render(request, 'your_app/flight_result.html', {'flights': flights})
    else:
        form = FlightSearchForm()
    return render(request, 'datapp/flight_search.html', {'form': form})

def get_city_suggestions(request):
    term = request.GET.get('term', '')
    origins = Flight.objects.filter(origin__icontains=term).values_list('origin', flat=True).distinct()
    destinations = Flight.objects.filter(destination__icontains=term).values_list('destination', flat=True).distinct()
    suggestions = list(set(origins) | set(destinations))  # Combine and deduplicate
    return JsonResponse(suggestions, safe=False)

```
THIS FUNCTION USES THE POST METHOD TO TO IMPORT THE INPUT WHICH I FILLS TO DJANGO ADMIN PANEL AND THEN SEARCH FOR THE SIMILARITY ACCORDING TO THE INPUTS 
THEN I HAVE SAVED THE ORIGIN AND DESTINATION IN FORM AND THEN USE FILTER METHOD TO FILED THE DATA ACCORDING THE DATABASE 
FIRST FUNCTION USED FOR FLIGHT SEARCHIND AND SECOND FUNCTION IS USED FOR CITY SUGGESTION OI HAVE ALSO USE SOME JAVASCRIPT TO GET THE CITY NAMES 




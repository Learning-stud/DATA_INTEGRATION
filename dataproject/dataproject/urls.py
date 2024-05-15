"""
URL configuration for dataproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from datapp import views  # Import your app's views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.flight_search, name='home'),  # Set the root URL to point to the flight_search view
    # path('search/', views.flight_search, name='flight_search'),
    # path('get_city_suggestions/', views.get_city_suggestions, name='get_city_suggestions'),
 path('admin/', admin.site.urls),
    path('', include('datapp.urls')),
]


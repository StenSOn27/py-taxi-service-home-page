from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from taxi.models import Car, Manufacturer, Driver


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "taxi/index.html", context=context)

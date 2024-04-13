from uuid import uuid4

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View

from cars.filters import CarFilter
from cars.forms import CarsForms
from cars.models import Car


class CarsListView(View):
    def get(self, request):
        filter_form = CarFilter(request.GET, request=request)

        return render(request, "cars/list.html", {
            "extraHeadContext": {
                "title": "Cars List"
            },
            "context": {
                "situation": request.GET.get("situation"),
                "titleOfPage": request.GET.get("situation", "").upper(),
                "filter": filter_form
            }
        })


class CarsCreateView(View):
    def post(self, request):
        create_form = CarsForms(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()

            return redirect(
                f"{reverse('cars-list')}?situation={request.POST.get('situation')}"
            )

        return render(request, "cars/form.html", {
            "extraHeadContext": {
                "title": "Cars Create"
            },
            "context": {
                "situation": request.GET.get("situation"),
                "titleOfPage": request.GET.get("situation", "").upper(),
                "form": create_form
            }
        })

    def get(self, request):
        create_form = CarsForms(
            initial={
                "car_id": str(uuid4())
            }
        )

        return render(request, "cars/form.html", {
            "extraHeadContext": {
                "title": "Cars Create"
            },
            "context": {
                "situation": request.GET.get("situation"),
                "titleOfPage": request.GET.get("situation", "").upper(),
                "form": create_form
            }
        })


class CarsDeleteView(View):
    def get(self, request, car_id):
        car = Car.objects.filter(car_id=car_id)
        car.delete()

        return redirect(
            f"{reverse('cars-list')}?situation={request.GET.get('situation')}"
        )


class CarDetailView(View):
    def get(self, request, car_id):
        car = get_object_or_404(Car, car_id=car_id)
        detail_form = CarsForms(detail=True, initial=car.to_dict())

        return render(request, "cars/form.html", {
            "extraHeadContext": {
                "title": "Cars Detail"
            },
            "context": {
                "situation": request.GET.get("situation"),
                "titleOfPage": car.situation.upper(),
                "mode": 'detail',
                "form": detail_form
            }
        })

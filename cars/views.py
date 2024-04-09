from django.shortcuts import render, redirect
from django.views.generic import View

from cars.filters import CarFilter
from cars.forms import CarsForms


class CarsListView(View):
    def get(self, request):
        filter_form = CarFilter(request.GET, request=request)

        return render(request, "cars/list.html", {
            "extraHeadContext": {
                "title": "Cars List"
            },
            "context": {
                "carType": request.GET.get("carType"),
                "titleOfPage": request.GET.get("carType", "").upper(),
                "filter": filter_form
            }
        })


class CarsCreateView(View):
    def post(self, request):
        create_form = CarsForms(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()

            return redirect('cars-list')

    def get(self, request):
        create_form = CarsForms()

        return render(request, "cars/form.html", {
            "extraHeadContext": {
                "title": "Cars Create"
            },
            "context": {
                "carType": request.GET.get("carType"),
                "titleOfPage": request.GET.get("carType", "").upper(),
                "form": create_form
            }
        })

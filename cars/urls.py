from django.urls import path
from cars.views import CarsListView, CarsCreateView

urlpatterns = [
    path('', CarsListView.as_view(), name='cars-list'),
    path('register/', CarsCreateView.as_view(), name='cars-create')
]

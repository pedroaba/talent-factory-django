from django.urls import path, re_path
from cars.views import CarsListView, CarsCreateView, CarsDeleteView, CarDetailView

urlpatterns = [
    path(r'', CarsListView.as_view(), name='cars-list'),
    path('register/', CarsCreateView.as_view(), name='cars-create'),
    path('<str:car_id>/', CarsDeleteView.as_view(), name='cars-delete'),
    path('<str:car_id>/detail', CarDetailView.as_view(), name='cars-detail')
]

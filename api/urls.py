from django.urls import path
from .views import ListCompany, DetailCompany, ListVacancy, DetailVacancy

app_name = 'api'

urlpatterns = [
    path('compania/', ListCompany.as_view(), name='list-companies'),
    path('compania/<int:pk>/', DetailCompany.as_view(), name='see-company'),
    path('vacante/', ListVacancy.as_view(), name='list-vacancies'),
    path('vacante/<int:pk>/', DetailVacancy.as_view(), name='see-vacancy'),
]

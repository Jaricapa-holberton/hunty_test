from django.urls import path
from .views import ListCompany, DetailCompany, ListVacancy, DetailVacancy

app_name = 'api'

urlpatterns = [
    path('compania/', ListCompany.as_view()),
    path('compania/<int:pk>/', DetailCompany.as_view()),
    path('vacante/', ListVacancy.as_view()),
    path('vacante/<int:pk>/', DetailVacancy.as_view()),
]

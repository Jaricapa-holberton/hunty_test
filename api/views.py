from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from .models import Company, Vacancy
from .serializate import CompanyToDictionary, VacancyToDictionary
from django.views.generic import ListView, DetailView


class ListCompany(ListView):
    """
    Creates a Company object for render a template that list all the companies
    """
    model = Company
    template_name = 'company_list.html'

    def get(self, request):
        # Multiple Blogs
        companies = Company.objects.all()
        tempcomps = []
        # Converting `QuerySet` to a Python Dictionary
        for i in range(len(companies)):
            tempcomps.append(CompanyToDictionary(companies[i]))

        return HttpResponse(json.dumps(tempcomps), content_type="application/json")


class DetailCompany(DetailView):
    """
    Creates a Company object for render a template that display a specific company
    """
    model = Company
    template_name = 'company_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.CompanyId = kwargs['pk']
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Add blog to context.
        """
        comp = Company.objects.get(CompanyId=int(kwargs['pk']))
        company = CompanyToDictionary(comp)
        return HttpResponse(json.dumps(company), content_type="application/json")


class ListVacancy(ListView):
    """
    Creates a Vacancy object for render a template that list all the vacancies
    """
    model = Vacancy
    template_name = 'vacancy_list.html'

    def get(self, request):
        # Multiple Blogs
        vacancies = Vacancy.objects.all()
        tempvacan = []
        # Converting `QuerySet` to a Python Dictionary
        for i in range(len(vacancies)):
            tempvacan.append(VacancyToDictionary(vacancies[i]))

        return HttpResponse(json.dumps(tempvacan), content_type="application/json")


class DetailVacancy(DetailView):
    """
    Creates a Vacancy object for render a template that display a specific vacancy
    """
    model = Vacancy
    template_name = 'vacancy_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.VacancyId = kwargs['pk']
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Add blog to context.
        """
        vacan = Vacancy.objects.get(VacancyId=int(kwargs['pk']))
        vacancy = VacancyToDictionary(vacan)
        return HttpResponse(json.dumps(vacancy), content_type="application/json")

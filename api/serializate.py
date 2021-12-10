from django.views import View
from django.http import JsonResponse
from datetime import datetime
from .models import Company, Vacancy


def CompanyToDictionary(company):
    """
    A utility function to convert object of type Company to a Python Dictionary
    """
    output = {}
    output["CompanyId"] = company.CompanyId
    output["Name"] = company.Name
    output["Link"] = company.Link
    output["Country"] = company.Country
    output["City"] = company.City
    output["DateAdded"] = company.DateAdded.strftime("%m/%d/%Y")
    output["ContactFirstName"] = company.ContactFirstName
    output["ContactLastName"] = company.ContactLastName
    output["ContactPhoneNumber"] = company.ContactPhoneNumber
    output["ContactEmail"] = company.ContactEmail

    return output


def VacancyToDictionary(vacancy):
    """
    A utility function to convert object of type Vacancy to a Python Dictionary
    """
    output = {}
    output["VacancyId"] = vacancy.VacancyId
    output["PositionName"] = vacancy.PositionName
    output["VacancyLink"] = vacancy.VacancyLink
    output["CompanyId"] = vacancy.CompanyId.CompanyId
    output["Salary"] = vacancy.Salary
    output["Skills"] = vacancy.Skills
    output["MaxExperience"] = vacancy.MaxExperience
    output["MinExperience"] = vacancy.MinExperience

    return output

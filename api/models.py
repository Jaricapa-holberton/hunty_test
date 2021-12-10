from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Company(TimeStampedModel, SoftDeletableModel):
    CompanyId = models.IntegerField()
    Name = models.CharField(max_length=100)
    Link = models.URLField()
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    DateAdded = models.DateField(serialize=True)
    ContactFirstName = models.CharField(max_length=100)
    ContactLastName = models.CharField(max_length=100)
    ContactPhoneNumber = models.CharField(max_length=100)
    ContactEmail = models.EmailField()
    
    def __str__(self):
        return self.Name


class Vacancy(TimeStampedModel, SoftDeletableModel):
    VacancyId = models.IntegerField()
    PositionName = models.CharField(max_length=100)
    VacancyLink = models.URLField()
    CompanyId = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    Salary = models.IntegerField()
    Skills = models.CharField(max_length=100)
    MaxExperience = models.IntegerField()
    MinExperience = models.IntegerField()

    def __str__(self):
        return self.PositionName
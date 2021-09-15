from django.db import models
from postgres_copy import CopyManager


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File id {self.id}'


class CovidData(models.Model):
    iso_code = models.CharField(max_length=200, null=True, blank=True)
    continent = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)
    total_cases = models.FloatField(null=True, blank=True)
    new_cases = models.FloatField(null=True, blank=True)
    new_cases_smoothed = models.FloatField(null=True, blank=True)
    total_deaths = models.FloatField(null=True, blank=True)
    new_deaths = models.FloatField(null=True, blank=True)
    new_deaths_smoothed = models.FloatField(null=True, blank=True)
    total_cases_per_million = models.FloatField(null=True, blank=True)
    new_cases_per_million = models.FloatField(null=True, blank=True)
    new_cases_smoothed_per_million = models.FloatField(null=True, blank=True)
    total_deaths_per_million = models.FloatField(null=True, blank=True)
    new_deaths_per_million = models.FloatField(null=True, blank=True)
    new_deaths_smoothed_per_million = models.FloatField(null=True, blank=True)
    reproduction_rate = models.FloatField(null=True, blank=True)
    icu_patients = models.FloatField(null=True, blank=True)
    icu_patients_per_million = models.FloatField(null=True, blank=True)
    hosp_patients = models.FloatField(null=True, blank=True)
    hosp_patients_per_million = models.FloatField(null=True, blank=True)
    weekly_icu_admissions = models.FloatField(null=True, blank=True)
    weekly_icu_admissions_per_million = models.FloatField(
        null=True, blank=True)
    weekly_hosp_admissions = models.FloatField(null=True, blank=True)
    weekly_hosp_admissions_per_million = models.FloatField(
        null=True, blank=True)
    new_tests = models.FloatField(null=True, blank=True)
    total_tests = models.FloatField(null=True, blank=True)
    total_tests_per_thousand = models.FloatField(null=True, blank=True)
    new_tests_per_thousand = models.FloatField(null=True, blank=True)
    new_tests_smoothed = models.FloatField(null=True, blank=True)
    new_tests_smoothed_per_thousand = models.FloatField(null=True, blank=True)
    positive_rate = models.FloatField(null=True, blank=True)
    tests_per_case = models.FloatField(null=True, blank=True)
    tests_units = models.CharField(max_length=200, null=True, blank=True)
    total_vaccinations = models.FloatField(null=True, blank=True)
    people_vaccinated = models.FloatField(null=True, blank=True)
    people_fully_vaccinated = models.FloatField(null=True, blank=True)
    total_boosters = models.FloatField(null=True, blank=True)
    new_vaccinations = models.FloatField(null=True, blank=True)
    new_vaccinations_smoothed = models.FloatField(null=True, blank=True)
    total_vaccinations_per_hundred = models.FloatField(null=True, blank=True)
    people_vaccinated_per_hundred = models.FloatField(null=True, blank=True)
    people_fully_vaccinated_per_hundred = models.FloatField(
        null=True, blank=True)
    total_boosters_per_hundred = models.FloatField(null=True, blank=True)
    new_vaccinations_smoothed_per_million = models.FloatField(
        null=True, blank=True)
    stringency_index = models.FloatField(null=True, blank=True)
    population = models.FloatField(null=True, blank=True)
    population_density = models.FloatField(null=True, blank=True)
    median_age = models.FloatField(null=True, blank=True)
    aged_65_older = models.FloatField(null=True, blank=True)
    aged_70_older = models.FloatField(null=True, blank=True)
    gdp_per_capita = models.FloatField(null=True, blank=True)
    extreme_poverty = models.FloatField(null=True, blank=True)
    cardiovasc_death_rate = models.FloatField(null=True, blank=True)
    diabetes_prevalence = models.FloatField(null=True, blank=True)
    female_smokers = models.FloatField(null=True, blank=True)
    male_smokers = models.FloatField(null=True, blank=True)
    handwashing_facilities = models.FloatField(null=True, blank=True)
    hospital_beds_per_thousand = models.FloatField(null=True, blank=True)
    life_expectancy = models.FloatField(null=True, blank=True)
    human_development_index = models.FloatField(null=True, blank=True)
    excess_mortality = models.FloatField(null=True, blank=True)
    median_age = models.FloatField(null=True, blank=True)

    objects = CopyManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-pk']

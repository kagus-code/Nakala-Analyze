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
     total_cases = models.IntegerField(null=True , blank=True)
     new_cases = models.IntegerField(null=True , blank=True)
     total_deaths = models.IntegerField(null=True , blank=True)
     new_deaths = models.IntegerField(null=True , blank=True)
     new_deaths_smoothed = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     total_cases_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     new_cases_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     new_cases_smoothed_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     total_deaths_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     new_deaths_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     new_deaths_smoothed_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     reproduction_rate = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     icu_patients = models.IntegerField(null=True , blank=True)
     icu_patients_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     hosp_patients = models.IntegerField(null=True , blank=True)
     hosp_patients_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     weekly_icu_admissions = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     weekly_icu_admissions_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     weekly_hosp_admissions = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     weekly_hosp_admissions_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     new_tests = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     total_tests = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     total_tests_per_thousand = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     new_tests_per_thousand = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     new_tests_smoothed_per_thousand = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     positive_rate = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     tests_per_case = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     tests_units = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     total_vaccinations = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     people_vaccinated = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     people_fully_vaccinated = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     total_boosters = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     new_vaccinations = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     new_vaccinations_smoothed = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     total_vaccinations_per_hundred = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     people_vaccinated_per_hundred = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     people_fully_vaccinated_per_hundred = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     total_boosters_per_hundred = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     new_vaccinations_smoothed_per_million = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     stringency_index = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     population = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     population_density = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     median_age = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     aged_65_older = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     aged_70_older = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     gdp_per_capita = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     extreme_poverty = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     cardiovasc_death_rate = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     diabetes_prevalence = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     female_smokers = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     male_smokers = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     handwashing_facilities = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     hospital_beds_per_thousand = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     life_expectancy = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     human_development_index = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     excess_mortality = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
     median_age = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
   

     objects = CopyManager()


     def __str__(self):
        return str(self.StockCode)

     class Meta:
        ordering = ['-pk']    

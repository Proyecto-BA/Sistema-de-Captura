# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Covid(models.Model):
    country_region = models.TextField(db_column='Country/Region', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    confirmed = models.IntegerField(db_column='Confirmed', blank=True, null=True)  # Field name made lowercase.
    deaths = models.IntegerField(db_column='Deaths', blank=True, null=True)  # Field name made lowercase.
    recovered = models.IntegerField(db_column='Recovered', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    new_cases = models.IntegerField(db_column='New cases', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_deaths = models.IntegerField(db_column='New deaths', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    new_recovered = models.IntegerField(db_column='New recovered', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deaths_100_cases = models.FloatField(db_column='Deaths / 100 Cases', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    recovered_100_cases = models.FloatField(db_column='Recovered / 100 Cases', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deaths_100_recovered = models.FloatField(db_column='Deaths / 100 Recovered', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    confirmed_last_week = models.IntegerField(db_column='Confirmed last week', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_1_week_change = models.IntegerField(db_column='1 week change', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    who_region = models.TextField(db_column='WHO Region', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    id = models.AutoField(primary_key=True)

    def Muertes(self):
            return self.deaths
            
    class Meta:
        managed = False
        db_table = 'country_wise_latest'

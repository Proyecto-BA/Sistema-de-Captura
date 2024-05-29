# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CountryWiseLatest(models.Model):
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
    number_1_week_increase = models.FloatField(db_column='1 week % increase', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    who_region = models.TextField(db_column='WHO Region', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'country_wise_latest'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

from django.db import models


class PlanetsParameters(models.Model):
    KSS = 1
    RSS = 2
    WORLD_CHOICES = (
        (KSS, 'Planets of Kerbal world'),
        (RSS, 'Planets of real(RSS) world'),
    )
    PLANET = 1
    SATELITE = 2
    OBJECT_TYPE = (
        (PLANET, 'Planet'),
        (SATELITE, 'Satelite'),
    )
    name = models.CharField(max_length=200)
    world_type = models.IntegerField(
        choices=WORLD_CHOICES, null=True, blank=True)
    type_of_object = models.IntegerField(
        choices=OBJECT_TYPE, null=True, blank=True)
    radius = models.IntegerField(null=True, blank=True)  # in m
    atmosphere_attitude = models.IntegerField(null=True, blank=True)  # in m
    mass = models.BigIntegerField(null=True, blank=True)  # in kg
    standard_gravitational_parameter = models.BigIntegerField(
        null=True, blank=True)  # in (km^3)/(s^2)
    day_time = models.IntegerField(null=True, blank=True)  # in seconds

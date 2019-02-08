from django.db import models


class PlanetsParameters(models.Model):
    KSS = 1
    RSS = 2
    WORLD_CHOICES = (
        (KSS, 'Planets of Kerbal world'),
        (RSS, 'Planets of real(RSS) world'),
    )
    PLANET = 1
    SATELLITE = 2
    OBJECT_TYPE = (
        (PLANET, 'Planet'),
        (SATELLITE, 'Satellite'),
    )
    name = models.CharField(max_length=200)
    world_type = models.PositiveSmallIntegerField(choices=WORLD_CHOICES)
    type_of_object = models.PositiveSmallIntegerField(choices=OBJECT_TYPE)
    radius = models.BigIntegerField()  # in meters
    atmosphere_attitude = models.IntegerField()  # in meters
    mass = models.DecimalField(max_digits=100, decimal_places=0)  # in kilograms
    standard_gravitational_parameter = models.DecimalField(max_digits=100, decimal_places=0)  # (km^3)/(s^2)
    day_time = models.BigIntegerField()  # in seconds

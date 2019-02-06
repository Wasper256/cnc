from django.db import models, migrations


def load_data(apps, schema_editor):
    Planets = apps.get_model("calc", "PlanetsParameters")

    Planets(
        name="Dres",
        world_type=1,
        type_of_object= 1,
        radius=138000,
        atmosphere_attitude=0,
        mass=321909370000000000000,
        standard_gravitational_parameter=21484489000,
        day_time=34825.305
        ).save()
    Planets(
        name="Duna",
        world_type=1,
        type_of_object= 1,
        radius=320000,
        atmosphere_attitude=50000,
        mass=4515427000000000000000,
        standard_gravitational_parameter=301363210000,
        day_time=65766.707
        ).save()
    Planets(
        name="Eeloo",
        world_type=1,
        type_of_object= 1,
        radius=210000,
        atmosphere_attitude=0,
        mass=11149224000000000000000,
        standard_gravitational_parameter=74410815000,
        day_time=19462.412
        ).save()
    Planets(
        name="Eeloo",
        world_type=1,
        type_of_object= 1,
        radius=210000,
        atmosphere_attitude=0,
        mass=11149224000000000000000,
        standard_gravitational_parameter=74410815000,
        day_time=19462.412
        ).save()
    Planets(
        name="Eve",
        world_type=1,
        type_of_object= 1,
        radius=700000,
        atmosphere_attitude=90000,
        mass=122439800000000000000000,
        standard_gravitational_parameter=8171730200000,
        day_time=81661.857
        ).save()
    Planets(
        name="Jool",
        world_type=1,
        type_of_object= 1,
        radius=6000000,
        atmosphere_attitude=200000,
        mass=4233212700000000000000000,
        standard_gravitational_parameter=282528000000000,
        day_time=36012.387
        ).save()
    Planets(
        name="Kerbin",
        world_type=1,
        type_of_object= 1,
        radius=600000,
        atmosphere_attitude=70000,
        mass=52915158000000000000000,
        standard_gravitational_parameter=3531600000000,
        day_time=21600
        ).save()
    Planets(
        name="Moho",
        world_type=1,
        type_of_object= 1,
        radius=250000,
        atmosphere_attitude=0,
        mass=2526331400000000000000,
        standard_gravitational_parameter=168609380000,
        day_time=2665723.4
        ).save()


class Migration(migrations.Migration):

    dependencies=[
        ('calc', '0002_auto_20190206_0913'),
    ]

    operations=[
        migrations.RunPython(load_data),
    ]

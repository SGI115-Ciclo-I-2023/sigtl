# Generated by Django 4.2 on 2023-06-09 21:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("seguridad", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accion",
            name="fecha",
            field=models.DateTimeField(),
        ),
    ]
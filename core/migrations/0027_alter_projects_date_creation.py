# Generated by Django 4.1.2 on 2023-01-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0026_alter_projects_date_creation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projects",
            name="date_creation",
            field=models.DateField(verbose_name="Дата договора"),
        ),
    ]

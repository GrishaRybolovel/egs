# Generated by Django 4.0.6 on 2023-01-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_projects_cost_alter_projects_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='doc',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='Документ'),
        ),
    ]

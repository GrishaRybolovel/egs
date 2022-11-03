# Generated by Django 4.0.6 on 2022-11-03 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_projects_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='done',
            field=models.DateTimeField(null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='doc',
            field=models.FileField(null=True, upload_to='uploads_messages/', verbose_name='Документ'),
        ),
    ]

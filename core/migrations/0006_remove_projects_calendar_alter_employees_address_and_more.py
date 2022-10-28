# Generated by Django 4.1.2 on 2022-10-27 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_employees_employee_to_task_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='calendar',
        ),
        migrations.AlterField(
            model_name='employees',
            name='address',
            field=models.CharField(blank=True, max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='attestation',
            field=models.CharField(blank=True, max_length=255, verbose_name='Аттестация'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='company',
            field=models.CharField(choices=[('GP', 'ГАЗСПЕЦПРОЕКТ'), ('NG', 'Не ГАЗСПЕЦПРОЕКТ')], default='GP', max_length=3, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='date_of_birth',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='date_of_start',
            field=models.DateField(verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='division',
            field=models.CharField(choices=[('GSP', 'ГАЗСПЕЦПРОЕКТ'), ('PTO', 'Производственно-технический отдел (ПТО)'), ('WGP', 'Водгазпроект')], default='GSP', max_length=3, verbose_name='Отделение'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.CharField(blank=True, max_length=255, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employee_to_task',
            field=models.ManyToManyField(blank=True, null=True, related_name='employees', to='core.projects', verbose_name='*'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='info_about_relocate',
            field=models.CharField(blank=True, max_length=511, verbose_name='Информация о переводе'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='inn',
            field=models.CharField(blank=True, max_length=256, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='last_name',
            field=models.CharField(blank=True, max_length=63, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.employees', verbose_name='Начальник'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='login',
            field=models.CharField(blank=True, max_length=255, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.CharField(max_length=63, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='passport',
            field=models.CharField(blank=True, max_length=256, verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='password',
            field=models.CharField(blank=True, max_length=255, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='phone',
            field=models.CharField(blank=True, max_length=255, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='post',
            field=models.CharField(blank=True, max_length=255, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='qualification',
            field=models.CharField(blank=True, max_length=255, verbose_name='Повышение квалификации'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='retraining',
            field=models.CharField(blank=True, max_length=255, verbose_name='Проф. подготовка'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='role',
            field=models.CharField(choices=[('DI', 'Директор'), ('ME', 'Менеджер/Инженер'), ('RA', 'Работник'), ('BU', 'Бухгалтер'), ('RN', 'Руководитель направления'), ('KS', 'Кадровый специалист')], default='RA', max_length=3, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='snils',
            field=models.CharField(blank=True, max_length=256, verbose_name='СНИЛС'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='status',
            field=models.BooleanField(verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='surname',
            field=models.CharField(max_length=63, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='address',
            field=models.CharField(blank=True, max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='contact',
            field=models.CharField(blank=True, max_length=255, verbose_name='Контактный человек'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='contract',
            field=models.CharField(blank=True, max_length=255, verbose_name='Договор'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='cost',
            field=models.IntegerField(blank=True, verbose_name='Цена обслуживания'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='date_creation',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата договора'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='date_notification',
            field=models.DateTimeField(verbose_name='Дата(для оповещения)'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='email',
            field=models.CharField(blank=True, max_length=255, verbose_name='Контактный e-mail'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='object_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='Тип объекта'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='phone',
            field=models.CharField(blank=True, max_length=255, verbose_name='Контактный телефон'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='seasoning',
            field=models.CharField(choices=[('Seas', 'Сезонная'), ('Fyea', 'Круглогодичная')], default='Seas', max_length=4, verbose_name='Сезонность'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('IWrk', 'В работе'), ('PNR', 'ПНР'), ('SOff', 'В работе'), ('SMR', 'СМР'), ('AOff', 'Аварийное откл.')], default='IWrk', max_length=4, verbose_name='Статус объекта'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='author',
            field=models.CharField(max_length=255, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='completion',
            field=models.DateTimeField(verbose_name='Срок выполнения'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(verbose_name='Дата создания'),
        ),
    ]

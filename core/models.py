from django.db import models

# Create your models here.

#One to many(Project might have multiple tasks, but task must have only one project)
from django.db.models import QuerySet


class Employees(models.Model):
    name = models.CharField(max_length=63)
    surname = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField
    date_of_start = models.DateField
    login = models.CharField(max_length=63)
    password = models.CharField(max_length=256)
    ROLE_IN_SYSTEM_CHOICES = [
        ('DI', 'Директор'),
        ('ME', 'Менеджер/Инженер'),
        ('RA', 'Работник'),
        ('BU', 'Бухгалтер'),
        ('RN', 'Руководитель направления'),
        ('KS', 'Кадровый специалист')
    ]
    role = models.CharField(max_length=2,
                            choices=ROLE_IN_SYSTEM_CHOICES,
                            default='RA')
    inn = models.CharField(max_length=256)
    snils = models.CharField(max_length=256)
    passport = models.CharField(max_length=256)
    COMPANY_CHOICES = [
        ('GP', 'ГАЗСПЕЦПРОЕКТ'),
        ('NG', 'Не ГАЗСПЕЦПРОЕКТ')
    ]
    company = models.CharField(max_length=2,
                            choices=COMPANY_CHOICES,
                            default='GP')
    DIVISION_CHOICES = [
        ('GSP', 'ГАЗСПЕЦПРОЕКТ'),
        ('PTO', 'Производственно-технический отдел (ПТО)'),
        ('WGP', 'Водгазпроект')
    ]
    division = models.CharField(max_length=2,
                               choices=DIVISION_CHOICES,
                               default='GSP')
    leader = models.ForeignKey(
        "self",
        on_delete=models.deletion.SET_NULL,
        related_name="leader",
        db_index=True,
        null=True,
        blank=False
    )
    post = models.CharField(max_length=255)
    info_about_relocate = models.CharField(max_length=511)
    attestation = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    retraining = models.CharField(max_length=255)
    status = models.BooleanField()


class Messages(models.Model):
    message = models.CharField()
    author = models.ForeignKey(
        "core.Employees",
        on_delete=models.deletion.SET_NULL
    )
    task = models.ForeignKey(
        "core.Tasks",
        on_delete=models.deletion.SET_NULL
    )



class Tasks(models.Model):
    author = models.CharField(max_length=255)
    created = models.DateTimeField()
    completion = models.DateTimeField()
    projects = models.ForeignKey(
        "core.Projects",
        on_delete=models.deletion.SET_NULL,
    )

    @property
    def messages(self) -> QuerySet[Messages]:
        return self.tasks.all()

    @property
    def employees(self) -> QuerySet[Employees]:
        return self.tasks.all()



class Projects(models.Model):
    STATUS_CHOICES = [
        ('IWrk', 'В работе'),
        ('PNR', 'ПНР'),
        ('SOff', 'В работе'),
        ('SMR', 'СМР'),
        ('AOff', 'Аварийное откл.')
    ]
    SEASONING_CHOICES = [
        ('Seas', 'Сезонная'),
        ('Fyea', 'Круглогодичная')
    ]

    name = models.CharField(max_length=255)
    contract = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now=True)
    date_notification = models.DateTimeField()
    object_type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    status = models.CharField(
        max_length=4,
        choices=STATUS_CHOICES,
        default='IWrk'
    )
    seasoning = models.CharField(
        max_length=4,
        choices=SEASONING_CHOICES,
        default='Seas'
    )
    cost = models.IntegerField()
    calendar = models.CharField(max_length=255)
    card = models.ForeignKey(
        "core.Cards",
        on_delete=models.deletion.SET_PROTECT
    )



    #One to many Tasks
    #Many to many Employees
    @property
    def tasks(self) -> QuerySet[Tasks]:
        return self.tasks.all()

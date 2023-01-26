from django.db import models

# Create your models here.

#One to many(Project might have multiple tasks, but task must have only one project)
from django.db.models import QuerySet


class Employees(models.Model):
    name = models.CharField(max_length=63, verbose_name='Имя')
    surname = models.CharField(max_length=63, verbose_name='Фамилия')
    last_name = models.CharField(max_length=63, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=255, blank=True, verbose_name='Телефон')
    email = models.CharField(max_length=255, blank=True, verbose_name='Почта')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    date_of_start = models.DateField(verbose_name='Дата начала')
    login = models.CharField(max_length=255, blank=True, verbose_name='Логин')
    password = models.CharField(max_length=255, blank=True, verbose_name='Пароль')
    ROLE_IN_SYSTEM_CHOICES = [
        ('DI', 'Директор'),
        ('ME', 'Менеджер/Инженер'),
        ('RA', 'Работник'),
        ('BU', 'Бухгалтер'),
        ('RN', 'Руководитель направления'),
        ('KS', 'Кадровый специалист')
    ]
    role = models.CharField(max_length=3,
                            choices=ROLE_IN_SYSTEM_CHOICES,
                            default='RA',
                            verbose_name='Роль')
    inn = models.CharField(max_length=256, blank=True, verbose_name='ИНН')
    snils = models.CharField(max_length=256, blank=True, verbose_name='СНИЛС')
    passport = models.CharField(max_length=256, blank=True, verbose_name='Паспорт')
    COMPANY_CHOICES = [
        ('GP', 'ГАЗСПЕЦПРОЕКТ'),
        ('NG', 'Не ГАЗСПЕЦПРОЕКТ')
    ]
    company = models.CharField(max_length=3,
                            choices=COMPANY_CHOICES,
                            default='GP',
                            verbose_name='Компания')
    DIVISION_CHOICES = [
        ('GSP', 'ГАЗСПЕЦПРОЕКТ'),
        ('PTO', 'Производственно-технический отдел (ПТО)'),
        ('WGP', 'Водгазпроект')
    ]
    division = models.CharField(max_length=3,
                               choices=DIVISION_CHOICES,
                               default='GSP',
                               verbose_name='Отделение')
    leader = models.ForeignKey(
        "self",
        on_delete=models.deletion.CASCADE,
        null=True,
        blank=True,
        verbose_name='Начальник'
    )
    post = models.CharField(max_length=255, blank=True, verbose_name='Должность')
    info_about_relocate = models.CharField(max_length=511, blank=True, verbose_name='Информация о переводе')
    attestation = models.CharField(max_length=255, blank=True, verbose_name='Аттестация')
    qualification = models.CharField(max_length=255, blank=True, verbose_name='Повышение квалификации')
    retraining = models.CharField(max_length=255, blank=True, verbose_name='Проф. подготовка')
    status = models.BooleanField(verbose_name='Статус')


    employee_to_task = models.ManyToManyField(
        "Tasks",
        related_name="employees",
        blank=True,
        verbose_name='Задания'
    )
    employee_to_project = models.ManyToManyField(
        "Projects",
        related_name="projects",
        blank=True,
        verbose_name='Объекты'
    )

    employee_to_document = models.ManyToManyField(
        "Documents",
        related_name="employee_to_doc",
        blank=True,
        verbose_name='Документы'
    )

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'



class Messages(models.Model):
    message = models.CharField(max_length=1024, verbose_name='Сообщение')
    author = models.ForeignKey(
        "Employees",
        on_delete=models.deletion.PROTECT,
        verbose_name='Автор'
    )
    task = models.ForeignKey(
        "Tasks",
        on_delete=models.deletion.PROTECT,
        related_name="messages",
        verbose_name='Задание'
    )

    time = models.DateTimeField(auto_now=True)

    doc = models.FileField(null=True, blank=True, upload_to='uploads_messages/', verbose_name='Документ')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'



class Tasks(models.Model):
    name = models.CharField(max_length=1023, verbose_name='Задание', blank=True)
    author = models.ForeignKey(
        "Employees",
        on_delete=models.deletion.CASCADE,
        verbose_name='Автор'
    )
    created = models.DateTimeField(verbose_name='Дата создания')
    completion = models.DateTimeField(verbose_name='Срок выполнения')
    done = models.DateTimeField(verbose_name='Дата выполнения', null=True, blank=True)
    projects = models.ForeignKey(
        "Projects",
        on_delete=models.deletion.PROTECT,
        related_name="tasks",
        verbose_name='Проект'
    )

    @property
    def messages(self) -> QuerySet[Messages]:
        return Messages.objects.filter(task__name=self.name).order_by('-author__date_of_birth')

    @property
    def employees(self) -> QuerySet[Employees]:
        return Employees.objects.filter(employee_to_task__name=self.name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'



class Projects(models.Model):
    STATUS_CHOICES = [
        ('IWrk', 'В работе'),
        ('PNR', 'ПНР'),
        ('SOff', 'Сезон откл.'),
        ('SMR', 'СМР'),
        ('AOff', 'Аварийное откл.')
    ]
    SEASONING_CHOICES = [
        ('Seas', 'Сезонная'),
        ('Fyea', 'Круглогодичная')
    ]

    name = models.CharField(max_length=255, verbose_name='Название')
    contract = models.CharField(max_length=255, blank=True, verbose_name='Договор')
    date_creation = models.DateTimeField(auto_now=True, verbose_name='Дата договора')
    date_notification = models.DateTimeField(verbose_name='Дата(для оповещения)')
    object_type = models.CharField(max_length=255, blank=True, verbose_name='Тип объекта')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес')
    contact = models.CharField(max_length=255, blank=True, verbose_name='Контактный человек')
    phone = models.CharField(max_length=255, blank=True, verbose_name='Контактный телефон')
    email = models.CharField(max_length=255, blank=True, verbose_name='Контактный e-mail')
    status = models.CharField(
        max_length=4,
        choices=STATUS_CHOICES,
        default='IWrk',
        verbose_name='Статус объекта'
    )
    seasoning = models.CharField(
        max_length=4,
        choices=SEASONING_CHOICES,
        default='Seas',
        verbose_name='Сезонность'
    )
    cost = models.IntegerField(blank=True, verbose_name='Цена обслуживания')

    project_to_document = models.ManyToManyField(
        "Documents",
        related_name="project_to_doc",
        blank=True,
        verbose_name='Документы'
    )

    def __str__(self):
        return self.name

    #One to many Tasks
    #Many to many Employees
    @property
    def tasks(self) -> QuerySet[Tasks]:
        return Tasks.objects.filter(projects__name=self.name)

    class Meta:
        verbose_name = 'Объекты'
        verbose_name_plural = 'Объекты'


class Documents(models.Model):

    ROLE_IN_SYSTEM_CHOICES = [
        ('WO', 'Без статуса'),
        ('CH', 'Черновик'),
        ('NS', 'На согласовании'),
        ('CU', 'Действующий'),
        ('CO', 'Завершённый'),
        ('RA', 'Расторгнутый'),
        ('AN', 'Аннулированный')
    ]

    name = models.CharField(max_length=255, verbose_name='Наименование документа')
    status = models.CharField(max_length=4,
                              choices=ROLE_IN_SYSTEM_CHOICES,
                              default='CU',
                              verbose_name='Статус')
    duration = models.DateField(verbose_name='Срок действия')
    doc = models.FileField(upload_to='uploads/', verbose_name='Документ')

    def __str__(self):
        return self.name

    @property
    def employees(self) -> QuerySet['Employees']:
        return self.employee_to_doc.all()

    @property
    def projects(self) -> QuerySet['Projects']:
        return self.project_to_doc.all()

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'

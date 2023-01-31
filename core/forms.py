from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Projects, Employees, Documents, Messages

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control form-control-user'}), max_length=255)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                          'class': 'form-control form-control-user'}), max_length=255)
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password',
                                                              'class': 'form-control form-control-user'}), max_length=255)
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Repeat Password',
                                                              'class': 'form-control form-control-user'}), max_length=255)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProjectForm(ModelForm):
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
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Название',
                                                             'class': 'form-control'}), max_length=255)
    contract = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Договор',
                                                             'class': 'form-control'}), max_length=255)
    date_creation = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y',
                                                                           attrs={'class' : 'form-control icon-calendar',
                                                                                  'type' : 'date'}))
    date_notification = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y',
                                                                               attrs={'class' : 'form-control',
                                                                                      'type' : 'date'}))
    object_type = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Тип объекта',
                                                             'class': 'form-control'}), max_length=255)
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Адрес',
                                                             'class': 'form-control'}), max_length=255)
    contact = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Контактный человек',
                                                             'class': 'form-control'}), max_length=255)
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Контактный телефон',
                                                             'class': 'form-control'}), max_length=255)
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Контактный e-mail',
                                                             'class': 'form-control'}), max_length=255)
    status = forms.ChoiceField(required=False, choices=STATUS_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    seasoning = forms.ChoiceField(required=False, choices=SEASONING_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    cost = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Цена обслуживания',
                                                             'class': 'form-control'}))
    class Meta:
        model = Projects
        fields = ['name', 'contract', 'date_creation', 'date_notification', 'object_type', 'address',
                  'contact', 'phone', 'email', 'status', 'seasoning', 'cost']


class DocumentForm(ModelForm):
    ROLE_IN_SYSTEM_CHOICES = [
        ('WO', 'Без статуса'),
        ('CH', 'Черновик'),
        ('NS', 'На согласовании'),
        ('CU', 'Действующий'),
        ('CO', 'Завершённый'),
        ('RA', 'Расторгнутый'),
        ('AN', 'Аннулированный')
    ]
    TYPE_CHOICES = [
        ('01', 'Договор'),
        ('02', 'Регистрация объекта в государственном реестре'),
        ('03', 'Правоустанавливающие документы'),
        ('04', 'Проектные документы'),
        ('05', 'Экспертиза'),
        ('06', 'Страхование'),
        ('07', 'Разрешительные документы и акты ввода в эксплуатацию'),
        ('08', 'Исполнительно-техническая документация по строительству'),
        ('09', 'Эксплуатационные документы'),
        ('10', 'Обучение персонала'),
        ('11', 'Документы сезонные в эксплуатационный период'),
        ('12', 'Нормативно-правовые акты'),
        ('13', 'Иные документы')
    ]

    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Наименование документа',
                                                             'class': 'form-control'}), max_length=255)
    status = forms.ChoiceField(required=False, choices=ROLE_IN_SYSTEM_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    doc_type = forms.ChoiceField(required=False, choices=TYPE_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    duration = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y',
                                                                               attrs={'class' : 'form-control',
                                                                                      'type' : 'date'}))
    doc = forms.FileField(required=False, widget=forms.FileInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Documents
        fields = ['name', 'status', 'doc_type', 'duration', 'doc']

class MessageForm(ModelForm):
    def __init__(self, **kwargs):
        self.task = kwargs.pop('task', None)
        self.author = kwargs.pop('author', None)
        super(MessageForm, self).__init__(**kwargs)

    def save(self, commit=True):
        obj = super(MessageForm, self).save(commit=False)
        obj.task = self.task
        obj.doc = self.data['doc']
        obj.author = self.author
        if commit:
            obj.save()
        return obj

    doc = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Messages
        fields = ['message', 'doc']
from django.db import models

# Create your models here.

#One to many(Project might have multiple tasks, but task must have only one project)
from django.db.models import QuerySet


class Tasks(models.Model):
    projects = models.ForeignKey(
        "core.Projects",
        on_delete=models.deletion.SET_NULL,
        related_name="projects",
        db_index = True,
        null = True,
        blank = False
    )
    pass


class Projects(models.Model):
    name = models.CharField(max_length=255)
    contract = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)
    tasks = models.ForeignKey(
        "core.Tasks",
        on_delete=models.deletion.SET_NULL,
        related_name="tasks",
        db_index=True,
        null=True,
        blank=False
    )
    calendar = models.CharField(max_length=255)
    card = models.ForeignKey(
        "core.Cards",
        on_delete=models.deletion.SET_PROTECT,
    )



    #One to many Tasks
    #Many to many Employees
    @property
    def tasks(self) -> QuerySet[Tasks]:
        return self.tasks.all()

class Employees(models.Model):
    pass


class Cards(models.Model):
    ...
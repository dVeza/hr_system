import uuid
from django.db import models


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class TimeTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Employee(TimeTracking):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True, max_length=255)
    gender = gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField()
    industry = models.ForeignKey(
        "Industry",
        related_name='employees',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    years_experience = models.IntegerField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-id']


class Industry(TimeTracking):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        db_index=True,
        max_length=255
    )
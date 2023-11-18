from django.db import models


class Industry(models.Model):
    pass

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=265)
    last_name = models.CharField(max_length=265)
    email = models.EmailField(blank=True, null=True)
    gender = models.Choices(
        coi
        blank=True,
        null=True
    )
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    industry = models.ForeignKey(
        Industry,
        related_name='employees',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ['-id']


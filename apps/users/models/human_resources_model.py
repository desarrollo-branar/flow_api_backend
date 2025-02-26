"""Human resources model."""

# Django
from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

# Utilities
from utils.main_model import MainModel
from petitions.models import Department, Company


class HumanResource(MainModel, models.Model):
    """HumanResource

    Args:
        MainModel (_type_): _description_
        models (_type_): _description_
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="human_resource",
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        related_name="hr_departments",
        null=True,
        blank=True
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name="hr_companies",
    )
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to="users/pictures", blank=True, null=True)

    def clean(self):
        """Evitar que los clientes (`Client`) tengan un departamento asignado."""
        if self.user.groups.filter(name="Client").exists() and self.department is not None:
            raise ValidationError("Los clientes no pueden tener un departamento asignado.")

    def save(self, *args, **kwargs):
        """Ejecuta la validación antes de guardar."""
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        indexes = [
            models.Index(fields=["-created"]),
            models.Index(fields=["active"]),
        ]
        db_table = "human_resources"

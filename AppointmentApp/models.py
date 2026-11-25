from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from AccountApp.models import Doctor, Patient


# Create your models here.
class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "En attente"
        CONFIRMED = "CONFIRMED", "Confirme"
        CANCELLED = "CANCELLED", "Canceled"

    rason = models.TextField()
    prescription = models.FileField(
        blank=True,
        upload_to="prescription/",
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="appointments",
    )

    def clean(self):
        super().clean()
        if self.appointment_date < timezone.now():
            raise ValidationError("La date du rendez-vous doit être dans le futur.")

    class Meta:
        ordering = ["-appointment_date"]
        constraints = [
            models.UniqueConstraint (
                fields=["doctor", "appointment_date"],
                name="unicite_patient-doctor-date",
                violation_error_message="Ce docteur possède déjà un rendez-vous à cette date.",
            )
        ]
    def __str__(self):
        return f"Le rendez-vous concerne {self.rason}"
from django.db import models
from AccountApp.models import Doctor,Patient

# Create your models here.
class Appointment(models.Model):
    rason=models.TextField()
    prescription=models.FileField(
        blank=True
        upload_to='prescription/'
    )
    class Status(models.TextChoices):
        PENDING="PENDING","En attente"
        CONFIRMED="CONFIRMED","Confirme"
        CANCELLED="CANCELLED","canceled"
    status= models.charField(max_length=10,choices=Status.choices,default=status.PENDING)
    duration_minutes=models.PositiveIntegreField(default=30)
    Created_at=models.dateTimeField(auto_now_add=True)
    updated_at=models.dateTimeField(auto_now=True)
    Appointment_date= models.dateTimeField()
    doctor= models.foreingKey(Doctor,on_delete=models.CASCADE,related_name='appointment')
    Patient= models.foreingKey(partient,on_delete=models.CASCADE,related_name='appointment')
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validator import MimLengthVlidator,MixLengthVlidator
from django.utils import timezone
from django.core.exceptions import Validattionerreur
# Create your models here.
class User(AbstractUser):
    pass
class Doctor(user):
    license_numbre = models.charField(max_length=6,unique=True,validator=[MimLengthVlidator(6)],validator=[MaxLengthVlidator(6)])
    phone= models.charField(max_length=8,validator=[number_validator])
    Created_at=models.dateTimeField(auto_now_add=True)
    updated_at=models.dateTimeField(auto_now=True)
    Speciality=models.ManyToManyField(
        "AccountApp.Speciality",
        related_name='doctors',
    )
number_validator=RegexValidator(
        regex=r'^d{8}$',
        message="le numero de telephone doit contenir exectement 8 chiffres. "
)
def validate_birth_date(v):
    ifv>=timezone.localdate():
        raise validationError(la date de na)
class Patient(user):
    national_id= models.charField(max_length=8,unique=True,validator=[number_validator])
    phone= models.charField(max_length=8,validator=[number_validator])
    birth_date= models.DateField()
    Created_at=models.dateTimeField(auto_now_add=True)
    updated_at=models.dateTimeField(auto_now=True)
class Speciality(models.Model):
    name=models.charField(max_length=225)
    Created_at=models.dateTimeField(auto_now_add=True)
    updated_at=models.dateTimeField(auto_now=True)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinimumLengthValidator,MaxLengthValidator
from django.utils import timezone
from django.core.exceptions import VAlidateionError 
# Create your models here.

class User(AbstractUser):
    pass
    


class Specialty(models.Model):
    name = models.CharField (max_length=255)
    created_at = models.DateTimerField(auto_now_add=True)
    update_at = models.DateTimerField(auto_now=True)
    


class Doctor (User):
    license_number =models.CharField (max_length=6 , unique=True,validators=[MinimumLengthValidator(6),MaxLengthValidator(6)])
    phone =models.CharField (max_length=8)
    created_at = models.DateTimerField(auto_now_add=True)
    update_at = models.DateTimerField(auto_now=True)
    specialities = models.ManyToManyField(
        Specialty,
        related_name='doctors',
    )
    
number_validator = RegexValidator(regex=r'^\d{8}$',
        messsage="Le numero de telephone doit contenir exactement 8 chiffres.",)

def validate_birth_date (v):
    if v>=timezone.localdate():
        raise ValidatorError ("La date de naissance ne peut pas etre dans le futur.")
class patient (User):
    national_id= models.CharField(max_length=8 ,unique=True , validators=[number_validator])
    phone = models.CharField(max_length,validators=[number_validator])
        
    birth_date= models.DateField()
    created_at = models.DateTimerField(auto_now_add=True)
    update_at = models.DateTimerField(auto_now=True)




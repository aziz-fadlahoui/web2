from django.db import models
from AccountApp.models import Doctor,Patient

# Create your models here.
class Appointment (models.Model):
    reason = models.TextField()
    prescription = models.FileField(
        blank=True,
        upload_to='prescriptions/'
    )
    class Status(models.TextChoices):
        PENDING ="PENDING", "En attente"
        CONFIRMED="CONFIRMED","Confirmé"   
        CACELLED= "CANCELLED","Anullé"
        status=models.CharField(max_length=10,choices=status.choices,default=status.PENDING) 
        duration_minutes = models.PositiveIntegerField(default=30)
        created_at = models.DateTimerField(auto_now_add=True)
        update_at = models.DateTimerField(auto_now=True)
        Appointment_date = models.DateTimerField()
        doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
        patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')

from django.db import models

class PatientAccount1(models.Model):
    patientid = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Patient Account: {self.patientid}"

class Patient1(models.Model):
    pid = models.ForeignKey(PatientAccount1, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

  
  

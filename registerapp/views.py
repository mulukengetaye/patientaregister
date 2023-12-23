import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
from .models import Patient1, PatientAccount1

def patientadd(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        # Generate the patient ID
        patient_id = str(random.randint(1000, 9999))

        with transaction.atomic():
            # Create a new PatientAccount object
            patient_account = PatientAccount1.objects.create(patientid=patient_id)

            # Create a new Patient object with the generated patient ID
            patient = Patient1.objects.create(pid=patient_account, first_name=first_name,
                                              last_name=last_name, date_of_birth=date_of_birth,
                                              email=email, phone_number=phone_number)
                                               

        context = {
            'patient_id': patient_id
        }

        return render(request, 'registerapp/patientadd.html', context)

    return render(request, 'registerapp/patientadd.html')
from django.shortcuts import render, redirect
from .models import Patient1
def upregister(request):
    if request.method == 'POST':
        # Get form data
        patient_id = request.POST['patient_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        
        # Check if patient ID exists in PatientAccount1 table
        if PatientAccount1.objects.filter(patientid=patient_id).exists():
            # Retrieve the patient account from the PatientAccount1 table
            patient_account = PatientAccount1.objects.get(patientid=patient_id)
            
            # Create a new Patient object with the provided patient ID
            patient = Patient1.objects.create(pid=patient_account, first_name=first_name,
                                              last_name=last_name, date_of_birth=date_of_birth,
                                              email=email, phone_number=phone_number)
            patient.save()
            
            # Redirect to a success page or another view
            return redirect('upregister')
        else:
            return redirect('patientadd')

    return render(request, 'registerapp/upregister.html')
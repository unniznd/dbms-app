from django.contrib import admin
from datamodel import models

@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vNum','vName']

@admin.register(models.Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['vType','vId','vName','vPlace','vNum','vAge']

@admin.register(models.Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['nId','nName','nPhone','vNum']

@admin.register(models.Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['pId','pName','pType','pAge','house','street','state',
                    'city','pincode','pno1','pno2','disease','nId','dor']


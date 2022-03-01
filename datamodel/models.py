from datetime import datetime
from django.db import models


class Vehicle(models.Model):
    vNum = models.IntegerField(primary_key=True)
    vName = models.CharField(max_length=100)
    date = models.DateField(auto_created=True, default=datetime.now)

    def __str__(self) -> str:
        return self.vName

class Volunteer(models.Model):
    vType = models.CharField(max_length=10)
    vId = models.IntegerField(primary_key=True)
    vName = models.CharField(max_length=100)
    vPlace = models.CharField(max_length=100)
    vNum = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    vAge = models.IntegerField()
    date = models.DateField(auto_created=True, default=datetime.now)


    def __str__(self) -> str:
        return self.vName

class Nurse(models.Model):
    nId = models.IntegerField(primary_key=True)
    nName = models.CharField(max_length=100)
    nPhone = models.IntegerField()
    vNum = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField(auto_created=True, default=datetime.now)

    def __str__(self) -> str:
        return self.nName

class Patient(models.Model):
    pId = models.IntegerField(primary_key= True)
    pName = models.CharField(max_length=100)
    pType = models.CharField(max_length=10)
    pAge = models.IntegerField()
    house = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    pno1 = models.IntegerField()
    pno2 = models.IntegerField()
    disease = models.CharField(max_length=100)
    nId = models.ForeignKey(Nurse,on_delete=models.CASCADE)
    dor = models.CharField(max_length=100)
    date = models.DateField(auto_created=True, default=datetime.now)


    def __str__(self) -> str:
        return self.pName

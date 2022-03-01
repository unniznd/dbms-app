
from django.shortcuts import render

from django.views.generic import CreateView, UpdateView, ListView
from datamodel.models import Patient, Nurse, Volunteer, Vehicle


def home(request):
    if request.method == "POST":
        vehicle = Vehicle.objects.filter(date = request.POST.get("date"))
        nurse = Nurse.objects.all()
        volunteer = Volunteer.objects.all()
        patient = Patient.objects.all()
        context = {
            "vehicle":vehicle,
            "nurse":nurse,
            "volunteer":volunteer,
            "patient":patient
        }
        return render(request,"home.html", context=context)
    
    
    return render(request,"home.html")

class VehicleView(CreateView):
    model = Vehicle
    fields = ['vNum','vName']
    template_name = 'vehicle/vehicle.html'
    success_url = '/vehicle/update/'

class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = ['vNum','vName']
    template_name = 'vehicle/vehicle.html'
    success_url = '/vehicle/update/'

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle/vehicle_listview.html'
    context_object_name = 'vehicles'
    
    def get(self, request):
        vehicles = Vehicle.objects.all()
        
        return render(request,"vehicle/vehicle_listview.html",{"vehicles":vehicles})


class NurseView(CreateView):
    model = Nurse
    fields = ['nId','nName','nPhone','vNum']
    template_name = "nurse/nurse.html"
    success_url = '/nurse/update/'

class NurseUpdate(UpdateView):
    model = Nurse
    fields = ['nId','nName','nPhone','vNum']
    template_name = "nurse/nurse.html"
    success_url = '/nurse/update/'

class NurseListView(ListView):
    model = Nurse
    template_name = 'nurse/nurse_listview.html'
    context_object_name = 'nurses'
    
    def get(self, request):
        nurses = Nurse.objects.all()
        
        return render(request,"nurse/nurse_listview.html",{"nurses":nurses})



class VolunteerView(CreateView):
    model = Volunteer
    fields = ['vType','vId','vName','vPlace','vNum','vAge']
    template_name = "volunteer/volunteer.html"
    success_url = '/volunteer/update/'

class VolunteerUpdate(UpdateView):
    model = Volunteer
    fields = ['vType','vId','vName','vPlace','vNum','vAge']
    template_name = "volunteer/volunteer.html"
    success_url = '/volunteer/update/'

class VolunteerListView(ListView):
    model = Volunteer
    template_name = 'volunteer/volunteer_listview.html'
    context_object_name = 'volunteers'
    
    def get(self, request):
        volunteers = Volunteer.objects.all()
        
        return render(request,"volunteer/volunteer_listview.html",{"volunteers":volunteers})


class PatientView(CreateView):
    model = Patient
    fields = ['pId','pName','pType','pAge','house','street','state',
              'city','pincode','pno1','pno2','disease','nId','dor']
    template_name = "patient/patient.html"
    success_url = '/patient/update/'

class PatientUpdate(UpdateView):
    model = Patient
    fields = ['pId','pName','pType','pAge','house','street','state',
              'city','pincode','pno1','pno2','disease','nId','dor']
    template_name = "patient/patient.html"
    success_url = '/patient/update/'


class PatientListView(ListView):
    model = Patient
    template_name = 'patient/patient_listview.html'
    context_object_name = 'patients'
    
    def get(self, request):
        patients = Patient.objects.all()
        
        return render(request,"patient/patient_listview.html",{"patients":patients})

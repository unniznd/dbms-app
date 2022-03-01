
from django.urls import path
from datamodel.views import (
    PatientView, VehicleView, NurseView, VolunteerView, VehicleUpdate, VehicleListView,
    NurseListView, NurseUpdate,VolunteerUpdate, VolunteerListView, PatientListView, PatientUpdate,
    home
)
urlpatterns = [
    path('',home),
    path('vehicle/', VehicleView.as_view(),name="v-add"),
    path('vehicle/update/', VehicleListView.as_view(), name="v"),
    path('vehicle/update/<pk>/', VehicleUpdate.as_view(),name="v-update"),
    
    path('nurse/', NurseView.as_view(),name="n-add"),
    path('nurse/update/', NurseListView.as_view(),  name="n"),
    path('nurse/update/<pk>/', NurseUpdate.as_view(),name="n-update"),
    
    path('volunteer/',VolunteerView.as_view(),name="vo-add"),
    path('volunteer/update/', VolunteerListView.as_view(), name="vo"),
    path('volunteer/update/<pk>/', VolunteerUpdate.as_view(),name="vo-update"),
    
    path('patient/',PatientView.as_view(),name="p-add"),
    path('patient/update/', PatientListView.as_view(), name="p"),
    path('patient/update/<pk>/', PatientUpdate.as_view(),name="p-update"),
]
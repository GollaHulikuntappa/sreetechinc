from django.urls import path
from decomm.views import decommphasedetails

urlpatterns = [
    path('details/', decommphasedetails),
]
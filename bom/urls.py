from django.urls import path
from bom.views import bomphasedetails

urlpatterns = [
    path('details/', bomphasedetails),
]
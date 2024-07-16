from django.shortcuts import render

# Create your views here.
def decommphasedetails(request):
    return render(request,'./decomm/decommphases.html')
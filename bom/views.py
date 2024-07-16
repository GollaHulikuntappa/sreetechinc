from django.shortcuts import render

# Create your views here.
def bomphasedetails(request):
    return render(request,'./bom/bomphases.html')
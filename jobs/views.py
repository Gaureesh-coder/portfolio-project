from django.shortcuts import render
from .models import JOB #Getting JOB objects 


# Create your views here.
def home(request):
    jobs = JOB.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
from django.shortcuts import render, get_object_or_404
from .models import Job
# Create your views here.


def home(request):
    return render(request, 'job/home.html', {'jobs': Job.objects})


def view(request, job_id):
    details = get_object_or_404(Job, pk=job_id)
    return render(request, 'job/view.html', {'detail': details})

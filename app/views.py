from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    achievements = Achievement.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    
    context = {'achievements': achievements, 'educations': educations, 'experiences': experiences, 'projects': projects}
    
    return render(request, 'app/index.html', context)
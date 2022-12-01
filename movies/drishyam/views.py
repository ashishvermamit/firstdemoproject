from django.shortcuts import render

# Create your views here.
from drishyam.models import drishyamModel

def renderindex(request):
    return render(request,"index.html")

from django.shortcuts import render
from .models import *

def home(request):
    homes = Home.objects.all()
    context = {
        'homes': homes
    }
    return render(request,'index.html',context)
from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    catg = Category.objects.filter(parent=None)
    context = {'catg':catg}    
    return render(request, 'index.html', context)
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
# from .models import Reservation
from gallery.models import Concept

def home(request):
    concepts = Concept.objects.all()   
    context = {
        'concepts': concepts  # Truyền danh sách concept vào template
    }
    return render(request, 'home.html',context)
def home_about(request):
    return render(request, 'home_about.html')

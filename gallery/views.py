from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render
from .models import Concept
import os
from django.conf import settings

def concept_gallery(request):
    # Lấy danh sách các concept từ database
    concepts = Concept.objects.all()
    
    context = {
        'concepts': concepts  # Truyền danh sách concept vào template
    }
    return render(request, 'home_gallery.html', context)

def concept_detail(request, folder_name):
    # Lấy danh sách các ảnh trong thư mục concept
    image_folder = os.path.join(settings.BASE_DIR, 'static/concepts', folder_name)
    images = os.listdir(image_folder)

    context = {
        'folder_name': folder_name,
        'images': images
    }
    return render(request, 'gallery_dt.html', context)
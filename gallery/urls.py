from django.urls import path, include
from .views import concept_gallery, concept_detail

urlpatterns = [
    path('', concept_gallery, name='concept_gallery'),  # URL cho gallery tổng
    path('<str:folder_name>/', concept_detail, name='concept_detail'),  # URL cho từng concept
]
from django.db import models

# Create your models here.
class Concept(models.Model):
    name = models.CharField(max_length=100)  # Tên concept
    folder_name = models.CharField(max_length=100)  # Tên thư mục chứa ảnh của concept

    def __str__(self):
        return self.name
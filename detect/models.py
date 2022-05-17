from django.db import models
from django.utils import timezone

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="Uploaded Files/",null=True)
    dateTimeOfUpload = models.DateTimeField()
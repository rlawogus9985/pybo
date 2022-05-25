from django.db import models
from django.utils import timezone

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.ImageField(upload_to="Uploaded/",null=True)
    dateTimeOfUpload = models.DateTimeField()

class Accuracy(models.Model):
    picture = models.ForeignKey(Document,on_delete=models.CASCADE)
    acc = models.IntegerField(default=0)

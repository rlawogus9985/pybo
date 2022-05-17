from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.utils import timezone
from .models import Document

def uploadFile(request):
    if request.method == "POST":
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile,
            dateTimeOfUpload = timezone.now(),
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "detect/upload-file.html", context={"files": documents})

def file_delete(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    document.delete()
    return redirect('/detect/')
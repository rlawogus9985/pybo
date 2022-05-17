from django.shortcuts import render
from . import models
from django.utils import timezone

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
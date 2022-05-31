from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.utils import timezone
from .models import Document, Accuracy
import random

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

def detail(request, file_id):
    question = get_object_or_404(Document, pk=file_id)
    number= random.randrange(1,101)
    context={"question":question, "number":number}
    return render(request, 'detect/question_detail.html', context)

def accuracy(request):
    # question = get_object_or_404(Document, pk=file_id)
    # answer = Accuracy(picture=question, acc=15)
    # answer.save()
    # context={"accuracy":answer.acc}
    # return render(request, 'detect/question_detail.html', context)
    number = random.randrange(0,101)
    return render(request, 'detect/question_detail.html', {'number':number})


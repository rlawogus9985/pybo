from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'detect'

urlpatterns = [
    path('', views.uploadFile, name='uploadFile'),
    path('delete/<int:document_id>/', views.file_delete, name='file_delete'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'detect'

urlpatterns = [
    path('', views.uploadFile, name='uploadFile'),
    path('delete/<int:document_id>/', views.file_delete, name='file_delete'),
    path('<int:file_id>/', views.detail, name='detail'),
    # 같은 path에 여러 view는 적용 못하나봄
    # path('<int:file_id>/', views.accuracy, name='accuracy')
]

urlpatterns += static(settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT)

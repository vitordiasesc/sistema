from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # 👈 Import necessário
from .views import criar_superuser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', include('alunos.urls')),
    path('criar-superuser/', criar_superuser, name='criar_superuser'),
]

# 👇 Adicione isso para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

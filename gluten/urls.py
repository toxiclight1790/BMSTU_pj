from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /5/
    path('<int:recept_id>/', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
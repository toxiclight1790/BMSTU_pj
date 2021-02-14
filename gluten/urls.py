from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name='index'),
    path('menu/', views.Menu, name='menu'),
    # ex: categor/5/
    path('categor/<int:categor_id>/', views.detail, name='detail'),
    # ex: recept/5/
    path('recept/<int:recept_id>/', views.CurRec, name='recept'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
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
    # ex: addrecept/
    path('addrecept/', views.NewRecView.as_view(), name='add'),
    # ex: delete/5/
    path('delete/<int:recept_id>/', views.DelRec, name='delete'),
    # ex: addcom/5/
    path('addcom/<int:recept_id>/', views.NewComView.as_view(), name='add_com'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
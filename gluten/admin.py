from django.contrib import admin
from .models import Recept, Text, Categor, Comment

admin.site.register(Recept)
admin.site.register(Text)
admin.site.register(Categor)
admin.site.register(Comment)
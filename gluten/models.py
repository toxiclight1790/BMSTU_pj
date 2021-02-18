from django.db import models
from django.utils.timezone import now

class Categor(models.Model):
    title = models.CharField(default='Test',max_length=200)

    def __str__(self):
        return self.title

class Recept(models.Model):
    name = models.CharField(default='',max_length=200)
    types = models.ForeignKey(Categor,default=0,on_delete=models.CASCADE)
    description = models.CharField(default='',max_length=200)
    pub_date = models.DateTimeField(default=now,blank=True)
    likes = models.IntegerField(default=0)
    img = models.ImageField(upload_to ='uploads/', default='none.png')

    def __str__(self):
        return self.name

class Text(models.Model):
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)
    recept_text = models.CharField(default='',max_length=200)
    img = models.ImageField(upload_to ='uploads/Recepts/', blank=True)

    def __str__(self):
        return self.recept_text
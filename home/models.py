from django.db import models

# Create your models here.
class mark1(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='')
    

    def __str__(self):
        return self.title
    
class mark2(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

class poster(models.Model):
    title2 = models.CharField(max_length=100)
    content2 = models.CharField(max_length=1000)
    image8 = models.ImageField(upload_to='')

    def __str__(self):
        return self.title2
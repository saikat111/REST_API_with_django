from django.db import models
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=30, blank=False)
    title = models.CharField(max_length=60, blank=True)
    image = models.ImageField(upload_to='categories_image', blank=False)
    date = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lessons(models.Model):
    title = models.CharField(max_length=60, blank=False)
    lecturer1 = models.CharField(max_length=10000, blank=False)
    lecturer2 = models.CharField(max_length=10000, blank=True)
    image_title1 = models.CharField(max_length=50, blank=True)
    image1 = models.ImageField(upload_to='lesson_image', blank=True)
    image_title2 = models.CharField(max_length=50, blank=True)
    image2 = models.ImageField(upload_to='lesson_image', blank=True)
    writer_name = models.CharField(max_length=20, blank=False)
    date = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


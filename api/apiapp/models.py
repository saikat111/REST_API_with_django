from django.db import models
# Create your models here.


class Categories(models.Model):
    your_choices = (
        ('1', u'c'),
        ('2', u'java'),
        ('3', u'python'),
        ('4', u'c++'),
        ('5', u'javascript'),
        ('6', u'php'),
        ('7', u'html'),
        ('8', u'css'),
        ('9', u'c#'),
        ('10', u'go'),
        ('11', u'Swift'),
        ('12', u'Dart'),
        ('13', u'Kotlin'),
        ('14', u'Ruby'),
        ('15', u'Kotlin '),
    )
    name = models.CharField(max_length=30, blank=False)
    title = models.CharField(max_length=60, blank=True)
    type = models.CharField(max_length=50, blank=False, choices=your_choices)
    image = models.ImageField(upload_to='categories_image', blank=False)
    date = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Lessons(models.Model):
    your_choices = (
        ('1', u'c'),
        ('2', u'java'),
        ('3', u'python'),
        ('4', u'c++'),
        ('5', u'javascript'),
        ('6', u'php'),
        ('7', u'html'),
        ('8', u'css'),
        ('9', u'c#'),
        ('10', u'go'),
        ('11', u'Swift'),
        ('12', u'Dart'),
        ('13', u'Kotlin'),
        ('14', u'Ruby'),
        ('15', u'Kotlin '),
    )
    title = models.CharField(max_length=60, blank=False)
    type = models.CharField(max_length=50, blank=False, choices=your_choices)
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
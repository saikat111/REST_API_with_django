# Generated by Django 3.1.5 on 2021-01-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0013_delete_lessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('lecturer', models.CharField(max_length=50)),
                ('image_title1', models.CharField(blank=True, max_length=50)),
                ('image1', models.ImageField(blank=True, upload_to='lesson_image')),
                ('image_title2', models.CharField(blank=True, max_length=50)),
                ('image2', models.ImageField(blank=True, upload_to='lesson_image')),
                ('writer_name', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

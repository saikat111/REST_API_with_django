# Generated by Django 3.1.5 on 2021-01-10 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(blank=True, max_length=60)),
                ('image', models.ImageField(upload_to='categories_image')),
                ('date', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

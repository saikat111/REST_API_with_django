# Generated by Django 3.1.5 on 2021-01-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0011_lessons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='lecturer',
            field=models.CharField(max_length=50),
        ),
    ]

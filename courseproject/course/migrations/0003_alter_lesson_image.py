# Generated by Django 4.2.16 on 2024-10-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_category_course_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(upload_to='lesson/%Y/%m/'),
        ),
    ]

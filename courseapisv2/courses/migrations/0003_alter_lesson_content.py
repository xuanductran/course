# Generated by Django 5.1.2 on 2024-10-27 09:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

# Generated by Django 3.0.5 on 2020-06-08 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_special_students_question_papers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='special_students',
            name='questions',
        ),
    ]

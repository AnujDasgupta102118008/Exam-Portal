# Generated by Django 3.0.5 on 2020-06-08 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200608_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='special_students',
            name='question_papers',
        ),
    ]

# Generated by Django 4.2.1 on 2023-08-29 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0003_alter_enrollment_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='file',
        ),
    ]

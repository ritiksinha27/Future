# Generated by Django 4.2.6 on 2023-10-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_course_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]

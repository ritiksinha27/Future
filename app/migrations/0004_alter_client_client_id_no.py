# Generated by Django 4.2.6 on 2023-10-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_client_id_student_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_id_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

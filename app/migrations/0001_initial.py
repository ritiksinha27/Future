# Generated by Django 4.2.6 on 2023-10-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.PositiveIntegerField()),
                ('client_id_no', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
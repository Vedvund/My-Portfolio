# Generated by Django 4.0.4 on 2022-05-29 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_projectdetails_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdetails',
            name='start_date',
        ),
    ]
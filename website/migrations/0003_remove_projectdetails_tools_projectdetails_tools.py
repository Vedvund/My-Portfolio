# Generated by Django 4.0.4 on 2022-05-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_projectdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdetails',
            name='Tools',
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='tools',
            field=models.ManyToManyField(blank=True, null=True, to='website.skill'),
        ),
    ]
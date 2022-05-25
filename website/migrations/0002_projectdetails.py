# Generated by Django 4.0.4 on 2022-05-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('github_link', models.CharField(blank=True, max_length=100, null=True)),
                ('website_link', models.CharField(blank=True, max_length=100, null=True)),
                ('icon_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('Tools', models.ManyToManyField(to='website.skill')),
            ],
        ),
    ]

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PersonalInfo(models.Model):
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    website_link = models.CharField(max_length=100, null=True, blank=True)
    github_link = models.CharField(max_length=100, null=True, blank=True)
    linkedin_link = models.CharField(max_length=100, null=True, blank=True)
    facebook_link = models.CharField(max_length=100, null=True, blank=True)
    instagram_link = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)


class SkillType(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.type


class Skill(models.Model):
    skill_type = models.ForeignKey('SkillType', on_delete=models.CASCADE, null=True, blank=True)
    skill_name = models.CharField(max_length=100, null=True, blank=True)
    skill_level = models.PositiveSmallIntegerField(help_text='Enter numbers between 0-100 only', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.skill_name


class ProjectDetails(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    tools = models.ManyToManyField('Skill', blank=True)
    github_link = models.CharField(max_length=100, blank=True, null=True)
    website_link = models.CharField(max_length=100, blank=True, null=True)
    icon_image = models.ImageField(null=True, blank=True)
    start_date = models.DateField(auto_now=True)

from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    user = User.objects.get(username='vedvund')
    personal_info = PersonalInfo.objects.get()
    skill_types = SkillType.objects.all()
    skills = Skill.objects.all().order_by('skill_name').order_by('skill_type')
    return render(request, 'website/index.html', {
        'user': user,
        'personal_info': personal_info,
        'skill_types': skill_types,
        'skills': skills,
    })

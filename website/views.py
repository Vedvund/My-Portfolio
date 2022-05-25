from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from django.contrib.auth.models import User
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from django.contrib import messages
from django.template.loader import get_template


class HomePage(View):
    try:
        context = {
            'user': User.objects.get(username='vedvund'),
            'personal_info': PersonalInfo.objects.get(),
            'skill_types': SkillType.objects.all(),
            'skills': Skill.objects.all().order_by('skill_name').order_by('skill_type'),
            'project_details': ProjectDetails.objects.all(),
        }
    except:
        context = {}

    @staticmethod
    def send_user_copy(contact_form):
        # Auto-Generate subject and message
        subject = f"Copy of your message to Vedavyas Vundyala"

        with open(str(settings.BASE_DIR) + "/templates/website/contactTemplate.txt") as f:
            mail_template = f.read()

        message = mail_template
        message = message.replace('[NAME]', contact_form['name'])
        message = message.replace('[PURPOSE]', contact_form['purpose'])
        message = message.replace('[MESSAGE]', contact_form['message'])
        message = message.replace('[DATE_TIME]', str(datetime.now()))

        # Send mail
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [contact_form['email'], 'vedvund@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        return True

    def get(self, request):
        return render(request, 'website/index.html', self.context)

    def post(self, request):
        if self.send_user_copy(request.POST):
            messages.success(request, 'Your Message Was Sent Successful...! Copy has been sent to the entered email id')
        else:
            messages.error(request, "Your Message wasn't Sent Successful...! Please Try Again...")
        return redirect(reverse('website:index') + '#contact')

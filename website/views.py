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
import requests
from dotenv import load_dotenv, find_dotenv
from decouple import config


def send_telegram_message(remote_address):
    BOT_TOKEN = config('TELEGRAM_BOT_TOKEN', default='abc')
    ADMIN_TELEGRAM_ID = config('ADMIN_TELEGRAM_ID', default='abc')
    BOT_API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    server_message = f"you got a visitor from {remote_address}"
    parameter = {
        "chat_id": ADMIN_TELEGRAM_ID,
        "text": server_message
    }
    requests.post(url=BOT_API, params=parameter)


class HomePage(View):
    template_name = 'website/index.html'

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

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        send_telegram_message(str(ip))

        return render(request, self.template_name, context)

    def post(self, request):
        if self.send_user_copy(request.POST):
            messages.success(request, 'Your Message Was Sent Successful...! Copy has been sent to the entered email id')
        else:
            messages.error(request, "Your Message wasn't Sent Successful...! Please Try Again...")
        return redirect(reverse('website:index') + '#contact')

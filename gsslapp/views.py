import logging
import smtplib

from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import InquiryForm
from .models import ContactInformation

logger = logging.getLogger(__name__)


def home(request):    
    contact = ContactInformation.objects.first()
    return render(request, "home/index.html", {"contact": contact})


@require_POST
def send_inquiry(request):
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    service = request.POST.get("service")
    message = request.POST.get("message")
    
    print(f"send_inquiry called with name: {name}, phone: {phone}, email: {email}, service: {service}, message: {message}")
    try:
        sent_count = send_mail(
            subject="New GSSL Website Inquiry",
            message= name + "\n" + phone + "\n" + email + "\n" + service + "\n" + message,
            from_email="monirul89@gmail.com",
            recipient_list=["mo7rul@gmail.com", "monir7team@gmail.com",],
            fail_silently=False,
        )
        sent_count = send_mail(
            subject=f"Thank you, {name}!",
            message= f'Thank you, {name}! Your registration for {service} has been' + ' successfully submitted. We will contact you soon.',
            from_email="monirul89@gmail.com",
            recipient_list=[email],
            fail_silently=False,
        )
    except Exception as e:
        logger.exception("Failed to send GSSL website inquiry email.")
        messages.error(request, f"Error: {e}")
    else:
        if sent_count:
            messages.success(request, "Thank you. Your inquiry has been sent.")
        else:
            messages.error(request, "Email backend did not send the message.")

    return redirect(f"{reverse('home')}#contact")
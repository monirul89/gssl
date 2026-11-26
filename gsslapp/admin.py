from django.contrib import admin
from .models import ContactInformation


@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ("phone_display", "email", "website_display")

from django.db import models


class ContactInformation(models.Model):
    phone_display = models.CharField(max_length=100)
    phone_link = models.CharField(max_length=30)
    email = models.EmailField()
    office_address = models.CharField(max_length=255)
    website_url = models.URLField()
    website_display = models.CharField(max_length=100)

    class Meta:
        verbose_name = "contact information"
        verbose_name_plural = "contact information"

    def __str__(self):
        return self.email

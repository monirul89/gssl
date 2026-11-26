from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import ContactInformation


class ContactInformationViewTests(TestCase):
    def test_home_displays_contact_information_from_database(self):
        ContactInformation.objects.all().delete()
        ContactInformation.objects.create(
            phone_display="01234-567890",
            phone_link="+8801234567890",
            email="contact@example.com",
            office_address="Test office address",
            website_url="https://example.com",
            website_display="example.com",
        )

        response = self.client.get(reverse("home"))

        self.assertContains(response, "01234-567890")
        self.assertContains(response, "contact@example.com")
        self.assertContains(response, "Test office address")
        self.assertContains(response, "https://example.com")


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    EMAIL_HOST_USER="sender@example.com",
    EMAIL_HOST_PASSWORD="test-password",
    DEFAULT_FROM_EMAIL="sender@example.com",
)
class SendInquiryTests(TestCase):
    def test_valid_submission_emails_both_recipients(self):
        response = self.client.post(
            reverse("send_inquiry"),
            {
                "name": "Test Customer",
                "phone": "01234-567890",
                "service": "corporate",
                "message": "Please contact me.",
            },
            follow=True,
        )

        self.assertRedirects(response, f"{reverse('home')}#contact")
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ["mo7rul@gmail.com", "monir7team@gmail.com"])
        self.assertIn("Name: Test Customer", mail.outbox[0].body)
        self.assertIn("Phone: 01234-567890", mail.outbox[0].body)
        self.assertIn("Service: Corporate Security", mail.outbox[0].body)
        self.assertIn("Please contact me.", mail.outbox[0].body)
        self.assertContains(response, "Your inquiry has been sent.")

    def test_invalid_submission_is_not_emailed(self):
        response = self.client.post(
            reverse("send_inquiry"),
            {
                "name": "Test Customer",
                "phone": "01234-567890",
                "service": "not-a-service",
                "message": "Please contact me.",
            },
            follow=True,
        )

        self.assertRedirects(response, f"{reverse('home')}#contact")
        self.assertEqual(len(mail.outbox), 0)
        self.assertContains(response, "Please complete all fields")

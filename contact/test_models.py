from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_contact_first_name_is_required(self):
        form = ContactForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0],
                         'This field is required.')

    def test_contact_email_address_is_required(self):
        form = ContactForm({'email_address': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email_address', form.errors.keys())
        self.assertEqual(form.errors['email_address'][0],
                         'This field is required.')

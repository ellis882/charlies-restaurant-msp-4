from django.test import TestCase
from events.forms import EventForm


class TestForms(TestCase):

    def test_event_form_with_valid_data(self):
        form = EventForm(data={
            'name': 'John',
            'email': 'Doe',
            'phone': 'email@email.com',
            'type_of_event': 'birthday partie',
            'number_of_persons': '34',
            'Date_of_event': '2022-10-10',
            'message': 'would like to book an event'
        })

        self.assertTrue(form.is_valid())

    def test_event_form_with_no_data(self):
        form = EventForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 7)

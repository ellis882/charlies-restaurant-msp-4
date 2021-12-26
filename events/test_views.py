from django.test import TestCase
from .views import event_reservation_form
from .forms import EventForm


class TestEventForm(TestCase):

    def test_event_reservation_form_is_valid(self):
        data = {
            'name': 'John',
            'email': 'Doe',
            'phone': 'email@email.com',
            'type_of_event': 'birthday partie',
            'number_of_persons': '34',
            'Date_of_event': '2022-10-10',
            'message': 'would like to book an event'

        }
        response = self.client.post('events/event.html', data=data)
        self.assertTemplateUsed(response, 'events/event.html')
        self.assertContains(response, 'name')
        self.assertContains(response, 'email')
        self.assertContains(response, 'phone')
        self.assertContains(response, 'type_of_event')
        self.assertContains(response, 'number_of_persons')
        self.assertContains(response, 'Date_of_event')
        self.assertContains(response, 'message')
        self.assertEqual(EventForm.objects.count(), 7)
        self.assertRedirects(response, 'contact:send_success')

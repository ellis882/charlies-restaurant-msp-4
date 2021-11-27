from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField()
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=150)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=2000)

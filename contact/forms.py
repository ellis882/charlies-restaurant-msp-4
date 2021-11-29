from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    from_email = forms.EmailField(required=True)
    phone = forms.CharField()
    subject = forms.CharField(required=True, max_length=300)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=1000)

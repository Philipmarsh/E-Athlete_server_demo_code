from django import forms

class TesterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=40, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label="Last name", max_length=40, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email_address = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    operating_system = forms.ChoiceField(choices=[('IOS', 'IOS'), ('Android', 'Android')])
    nda_check = forms.BooleanField(required=True)


class ContactForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=40, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label="Last name", max_length=40, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email_address = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Message'}))
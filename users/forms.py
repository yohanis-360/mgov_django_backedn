from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Developer
from captcha.fields import CaptchaField

class UserRegistrationForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=15)
    username = forms.CharField(max_length=150)
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    agree_to_terms = forms.BooleanField(required=True)
    captcha = CaptchaField()  # Add reCAPTCHA field

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password1', 'password2','username', 'mobile_number', 'date_of_birth', 'gender', 'captcha']
        help_texts = {
            'password1': '',
            'password2': '',
        }  # Suppress help texts

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        # Optionally, you can set help texts to empty if they still appear
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class DeveloperRegistrationForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = [
            'organization_name',
            'organization_address',
            'organization_website',
            'city',
            'woreda',
            'zone',
            'sub_city',
            'business_registration_number',
            'status'
        ]

class EmailVerificationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}),
        label="Email"
    )
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm, SetPasswordForm)
from .models import UserBase
from django_countries.fields import CountryField


class UserLoginForm(AuthenticationForm):
    """Custom login form """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):
    """Registration form for a new user."""
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100,
                             help_text='Required',
                             error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email', 'password', 'password2')

    def clean_user_name(self):
        """Validator, checks if the username is already exists in DB"""
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        """Validator, checks if password was correctly typed in twice"""
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        """Validator, checks if the email is already exists in DB"""
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, that is already taken')
        return email

    #  setting up forms fields look
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update({'class': 'form-control mb-3',
                                                      'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control mb-3',
                                                  'placeholder': 'E-mail',
                                                  'name': 'email',
                                                  'id': 'id_email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control mb-3',
                                                     'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Repeat Password'})


class PwdResetForm(PasswordResetForm):
    """Password reset form"""
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        """Checks if there is the e_mail in the database"""
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError('Unfortunately we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    """Form for creating a new password. Validation is already prebuild in Django!"""
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))


class UserEditForm(forms.ModelForm):
    """Edit users details form, page: change details"""

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-user_name', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-first_name'}))

    about = forms.CharField(
        label='About', max_length=500, widget=forms.Textarea(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Some information about me', 'id': 'form-about'}))
    # Delivery details
    country = CountryField().formfield()

    phone_number = forms.CharField(
        label='Phone number', max_length=40, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'id': 'form-Phone_number'}))
    postcode = forms.CharField(
            label='postcode', max_length=40, widget=forms.TextInput(
                attrs={'class': 'form-control mb-3', 'id': 'form-postcode'}))
    address_line_1 = forms.CharField(
            label='address_line_1', max_length=40, widget=forms.TextInput(
                attrs={'class': 'form-control mb-3', 'id': 'form-address_line_1'}))
    address_line_2 = forms.CharField(
            label='address_line_2', max_length=40, widget=forms.TextInput(
                attrs={'class': 'form-control mb-3', 'id': 'form-address_line_2'}))
    town_city = forms.CharField(
            label='town_city', max_length=40, widget=forms.TextInput(
                attrs={'class': 'form-control mb-3', 'id': 'form-town_city'}))

    class Meta:
        model = UserBase
        fields = ('email', 'user_name', 'first_name', 'about', 'country',
                  'phone_number', 'postcode', 'address_line_1', 'address_line_2', 'town_city', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True

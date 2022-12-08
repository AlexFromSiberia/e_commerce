from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from orders.views import user_orders
from .forms import RegistrationForm, UserEditForm
from .models import UserBase
from .tokens import account_activation_token
from django.core.mail import send_mail
from core.settings import sender_mail


@login_required
def dashboard(request):
    """Page: Dashboard. Login is required."""
    orders = user_orders(request)
    return render(request, 'account/dashboard/dashboard.html', {'section': 'profile', 'orders': orders})


@login_required
def edit_details(request):
    """Page: Edit details. """
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, 'account/user/edit_details.html', {'user_form': user_form})


@login_required
def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirmation')


def account_register(request):
    """New user registration page + sending an activation e_mail"""
    if request.user.is_authenticated:
        # if user is registered already, redirect to dashboard
        return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            # at first new user is not active. Activation will be done through e_mail
            user.is_active = False
            user.save()
            # Setup e_mail
            # Gets current domain
            current_site = get_current_site(request)
            subject = 'Activation link has been sent to your email id'
            # the e_mail message is formed from html code: account_activation_email.html
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # sending an activation link via e_mail
            # Put here your sender_mail address(and check e_mail settings in SETTINGS.py):
            sender = sender_mail
            receiver_mail = user.email
            mail = send_mail(subject, message, sender, [receiver_mail], fail_silently=False)
            return render(request, 'account/registration/register_email_confirm.html')
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    """Checks if the link user used is original, then activates new user account"""
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # Note that data set during the anonymous session is retained when the user logs in.
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')



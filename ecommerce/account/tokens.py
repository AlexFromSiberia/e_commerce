from django.contrib.auth.tokens import PasswordResetTokenGenerator
# this one we need for TokenGenerator proper work. Reed more:
# https://pypi.org/project/six/
# https://pythonpip.ru/django/registratsiya-polzovatelya-django-s-podtverzhdeniem-po-email
from six import text_type


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """Creation of activation tokens for e_mails, which will be sent to all new users"""
    def _make_hash_value(self, user, timestamp):
        return text_type(user.pk) + text_type(timestamp) + text_type(user.is_active)


account_activation_token = AccountActivationTokenGenerator()

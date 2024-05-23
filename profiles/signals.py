from django.core.mail import send_mail
from django.dispatch import receiver
from allauth.account.signals import password_changed
from django.template.loader import render_to_string
from django.conf import settings


@receiver(password_changed)
def send_password_change_email(sender, user, **kwargs):
    '''
    Send an email to the user when their password is changed
    '''
    subject = 'Password Changed Successfully!'
    message = render_to_string(
        'password_changed_message_modified.txt', {'user': user})
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

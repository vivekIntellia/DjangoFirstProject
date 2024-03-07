from django.core.mail import send_mail
from django.conf import settings

def send_mail_to_user():
    subject = "Conformation mail"
    message = "This is the conformation mail that you have received.Thank You for filing the form , we appreciate your interest in joning us for now just wait for the administration to approve your request. We will get to you soon "
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["vivekyadav2750@gmail.com"]
    send_mail(subject , message , from_email , recipient_list )
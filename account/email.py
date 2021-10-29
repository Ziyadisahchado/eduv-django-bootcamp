from django.core.mail import BadHeaderError, send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string


def send_confirnation_email(instance):
    # Generate token and encode user primary key
    token = default_token_generator.make_token(instance)
    uid = urlsafe_base64_encode(force_bytes(instance.pk))

    # Send the email
    subject = "Account Acctivation"
    url = f"http://eduvjobs.herokuapp.com/activate/{uid}/{token}?status=new"
    html_message = f"""<div style="margin: 5% 0%;">

            <h2>Welcome to Eduv Job Portal</h2>
            Hello {instance.first_name}, <br><br>As a form of avoiding unrealistic,unseriuos users and for security precautions,we have to ensure email confirmation.<br><br>
                Please click on the link below to confirm your registration, Just ignore if you did not sign up for Eduv Job Portal<br><br><a href=\"{url}\" style="color:white; text-decoration: none;border-radius: 25px; background-color: #754C28; padding: 7px 25px;"> <strong>Verify Email<strong></a>
            </div>"""

    email_content = ""
    try:
        send_mail(subject, email_content, "helpraisemyfund@gmail.com",
                  [instance.email], fail_silently=False, html_message=html_message)
        return 'email sent successfully'
    except BadHeaderError:
        return 'email not sent'


def new_recuiter(instance):
    # Send the email
    subject = "New Recuiter Alert"
    url = f"http://eduvjobs.herokuapp.com/clear-recuiter/pk={instance.id}/"
    html_message = f"""<div style="margin: 5% 0%;">

            <h2>New Recuiter Alert</h2>
            Hello Admin, <br><br> 
            You have new recuiter to clear waiting to post jobs<br><br>
            <div>Recuiter: {instance.company_name}</div>
            <div>Website: {instance.website}</div>
            <br><br><a href=\"{url}\" style="color:white; text-decoration: none;border-radius: 25px; background-color: #754C28; padding: 7px 25px;"> <strong>Activate Recuiter<strong></a>
            </div>"""

    email_content = ""
    try:
        send_mail(subject, email_content, "helpraisemyfund@gmail.com",
                  ["helpraisemyfund@gmail.com"], fail_silently=False, html_message=html_message)
        return 'email sent successfully'
    except BadHeaderError:
        return 'email not sent'

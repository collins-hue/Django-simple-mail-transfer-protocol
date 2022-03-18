# Django-simple-mail-transfer-protocol

This is a django SMTP. for every subscriber, we'll alert him/her.

# Sending email¶

Although Python provides a mail sending interface via the smtplib module, Django provides a 
couple of light wrappers over it. These wrappers are provided to make sending email extra quick,
to help test email sending during development,
and to provide support for platforms that can’t use SMTP.

The code lives in the django.core.mail module.

Mail is sent using the SMTP host and port specified in the EMAIL_HOST and EMAIL_PORT settings.
The EMAIL_HOST_USER and EMAIL_HOST_PASSWORD settings, if set, are used to authenticate to the SMTP server, 
and the EMAIL_USE_TLS and EMAIL_USE_SSL settings control whether a secure connection is used.

# send_mail()¶
send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)[source]¶
In most cases, you can send email using django.core.mail.send_mail().

The subject, message, from_email and recipient_list parameters are required.

subject: A string.

message: A string.

from_email: A string. If None, Django will use the value of the DEFAULT_FROM_EMAIL setting.

recipient_list: A list of strings, each an email address. Each member of recipient_list will see the other recipients in the “To:” field of the email message.

fail_silently: A boolean. When it’s False, send_mail() will raise an smtplib.SMTPException if an error occurs. See the smtplib docs for a list of possible exceptions, all of which are subclasses of SMTPException.

auth_user: The optional username to use to authenticate to the SMTP server. If this isn’t provided, Django will use the value of the EMAIL_HOST_USER setting.

auth_password: The optional password to use to authenticate to the SMTP server. If this isn’t provided, Django will use the value of the EMAIL_HOST_PASSWORD setting.

connection: The optional email backend to use to send the mail. If unspecified, an instance of the default backend will be used. See the documentation on Email backends for more details.

html_message: If html_message is provided, the resulting email will be a multipart/alternative email with message as the text/plain content type and html_message as the text/html content type.

The return value will be the number of successfully delivered messages (which can be 0 or 1 since it can only send one message).

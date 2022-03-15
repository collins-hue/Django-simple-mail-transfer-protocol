from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from smtp.settings import EMAIL_HOST_USER

from mail.forms import SubscribeForm
from mail.models import Subscriber


def index(request):
    subform = SubscribeForm()
    html = "<html><body>Great moments at the moment</body></html>"

    print ('Load successful')
    if request.method == 'POST':
        sub_email = Subscriber(email=request.POST['email'])
        sub_email.save()
        subject = 'Hello There'
        message = '<html><body color:green >Have you Read the Nicomachean Ethics. <br>It is one of Aristotles greatest worlks.</body><html>'
        recipient = str(sub_email.email)
        send_mail(subject, message,
                  EMAIL_HOST_USER,
                  [recipient],
                  fail_silently=False)

        return HttpResponse(html)
    return render(request, 'index.html', {'subform': subform,} )

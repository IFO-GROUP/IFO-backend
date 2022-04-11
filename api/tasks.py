from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import threading


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_mail(Subscriber):

    body =render_to_string('email.html', context={
        'subscriber_email':Subscriber.email,
    })
    
    msg = EmailMessage(subject='New Subscribers', body=body,
        from_email=settings.EMAIL_HOST_USER, to=['ifo.corporation2020@gmail.com', 'info@ifocorporation.com','gandabhasan@gmail.com'], )
    
    msg.content_subtype = 'html'
    
    EmailThread(msg).start()
    print('email sent successfully')
    
    
    
    



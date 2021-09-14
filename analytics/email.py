from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_activation_email(name,receiver,id):
    # Creating message subject and sender
    subject = 'Welcome to Our Nakala analaytics Application'
    sender = 'ekmuraya@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/activation.txt',{"name": name,"id": id})
    html_content = render_to_string('email/activation.html',{"name": name,"id": id})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from home.forms import ContactForm
from talent_factory import settings


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {
            'extraHeadContext': {
                'title': 'Home'
            }
        })


class ContactView(View):
    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = f'{contact_form.data.get("name")} está entrando em contato'
            message = contact_form.data.get("message")
            email_from = contact_form.data.get("email")
            email_to = settings.EMAIL_HOST_USER

            send_mail(
                subject,
                message,
                email_from,
                [email_to],
                fail_silently=True
            )
            return redirect('home')

        return render(request, "contact.html", {
            'extraHeadContext': {
                'title': 'Contact'
            },
            'context': {
                'situation': 'contact',
                'form': contact_form
            }
        })

    def get(self, request):
        contact_form = ContactForm()

        return render(request, "contact.html", {
            'extraHeadContext': {
                'title': 'Contact'
            },
            'context': {
                'situation': 'contact',
                'form': contact_form
            }
        })

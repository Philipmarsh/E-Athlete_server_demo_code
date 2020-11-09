import json
import smtplib
import ssl

from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from .forms import TesterForm, ContactForm
from .models import BlogPost
from django.conf import settings


class HomePageView(View):
    form_class = TesterForm
    initial = {'key': 'value'}
    template_name = 'home/homepage.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            message = f"Subject: {form.data['first_name']} {form.data['last_name']} would like to be a tester\n\n" \
                      f" {form.data['first_name']} {form.data['last_name']} would like to be a tester \n" \
                      f"their email address is {form.data['email_address']} and they have an " \
                      f"{form.data['operating_system']} phone.\n" \
                      f"yours faithfully,\nThe E-Athlete site"

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(settings.SYSTEM_EMAIL, settings.EMAIL_PASSWORD)
                server.sendmail(settings.SYSTEM_EMAIL, settings.SYSTEM_EMAIL, message)
                if form.data['operating_system'] == 'IOS':
                    message_with_apple = f"Subject: Link for testing E-Athlete\n\n" \
                                         f"Dear {form.data['first_name']}\n\nThank you very much for agreeing to " \
                                         f"take part in the" \
                                         f"testing phase of our product development. We would like to invite you" \
                                         f" to download the app" \
                                         f"from the link below:\n\n" \
                                         f"{settings.TESTFLIGHT_LINK}\n\n" \
                                         f"For any feedback, please either reply to this email, or contact us on our" \
                                         f" website.\n" \
                                         f"Best wishes\nThe E-Athlete Team"
                    server.sendmail(settings.SYSTEM_EMAIL, form.data['email_address'], message_with_apple)
                    thank_you_message = 'Thank you very much for participating in our tests, you should now ' \
                                        'receive an email ' \
                                        'with a link to download the app. Please check your spam folder if you do ' \
                                        'not see it.'
                    messages.success(request, thank_you_message)
                else:
                    thank_you_message = 'Thank you very much for participating in our tests, you should receive an ' \
                                        'email' \
                                        'shortly with a link to download our app'
                    messages.success(request, thank_you_message)

            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})


class ContactUsView(View):
    template_name = 'home/contact_us.html'
    homepage_name = 'home/homepage.html'
    form_class = ContactForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            message = f" Subject: New Message\n\nMessage From: {form.data['first_name']} " \
                      f"{form.data['last_name']}\n{form.data['email_address']}\n\n" + \
                      form.data['message']
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(settings.SYSTEM_EMAIL, settings.EMAIL_PASSWORD)
                server.sendmail(settings.SYSTEM_EMAIL, settings.SYSTEM_EMAIL, message)
            messages.success(request, 'Thank you for your message, we will reply to you soon.')
            return render(request, self.homepage_name, {'form': form})
        return render(request, self.template_name, {'form': form})


class BlogView(ListView):
    model = BlogPost
    paginate_by = 10
    queryset = BlogPost.objects.order_by('-created')
    template_name = 'home/blog.html'


class ProductsView(TemplateView):
    template_name = 'home/products.html'


class AboutUsView(TemplateView):
    template_name = 'home/about_us.html'


class NDAView(TemplateView):
    template_name = 'home/nda.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'home/privacy_policy.html'

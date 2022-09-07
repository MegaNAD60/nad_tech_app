from django.views.generic import TemplateView
from sendemail.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context=super(HomePageView, self ).get_context_data(*args, **kwargs)
        context['form'] = ContactForm

        return context
    
    def contactView(request):
        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']
                try:
                    send_mail(subject, message, from_email, ['admin@example.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('success')
        return render(request, "home.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


class PricingPageView(TemplateView):
    template_name = 'pricing.html'
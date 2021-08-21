from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    A view to return the contact page
    """
    if request.method == 'POST':

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message Sent!')
            return redirect(reverse('contact'))

        else:
            messages.error(request, 'Please check your form is valid.\
                Message send failed.')

    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'

    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)

from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm


# View for the About Me page
def about_me(request):

    """Hanles POST request for contact form submission"""
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Contact request received! I endeavour to respond within 2 working days."
            )

    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "contact_form": contact_form
         },
    )

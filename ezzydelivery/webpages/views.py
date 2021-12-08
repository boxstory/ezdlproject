from django.forms.fields import DateTimeField
from django.shortcuts import redirect, render
from webpages.forms import ContactForm
from django.core.mail import mail_admins

# Create your views here.


def index(request):
    data = {

    }
    return render(request, 'webpages/index.html', data)


def about(request):
    data = {

    }
    return render(request, 'webpages/about.html', data)


def services(request):
    data = {

    }
    return render(request, 'webpages/services.html', data)


def join_driver(request):
    data = {

    }
    return render(request, 'webpages/join_driver.html', data)


def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():

            name = f.cleaned_data['name']
            email = f.cleaned_data['email']
            mobile = f.cleaned_data['mobile']
            purpose = f.cleaned_data['purpose']

            message = f.cleaned_data['message']
            f = ContactForm(name=name, email=email, mobile=mobile,
                            purpose=purpose, message=message)
            f.save()

            return redirect('/')

    else:
        f = ContactForm()

    return render(request, 'webpages/contact.html', {'form': f})


def privacy(request):
    data = {

    }
    return render(request, 'webpages/privacy.html', data)

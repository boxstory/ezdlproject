from django.shortcuts import render

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


def contact(request):
    data = {

    }
    return render(request, 'webpages/contact.html', data)


def privacy(request):
    data = {

    }
    return render(request, 'webpages/privacy.html', data)

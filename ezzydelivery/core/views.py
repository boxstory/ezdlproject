from django.shortcuts import render

# Create your views here.

def profile(request):
    data = {

    }
    return render(request, 'core/profile.html', data)
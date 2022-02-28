from multiprocessing import context
from PIL import Image
from django.shortcuts import get_object_or_404, redirect, render
from core.models import *
from core.forms import *


# Create your views here.

def profile_view(request):
    user_id = request.user.id

    if Profile.objects.filter(user_id=user_id).exists():

        pk = request.user.id

        return redirect('core:profile', pk=pk)
    else:
        return redirect('core:profile_add')


def profile(request, pk):
    profile = get_object_or_404(Profile, user_id=request.user.id)
    context = {}
    context["profile"] = Profile.objects.get(user_id=request.user.id)
    return render(request, 'core/profile.html', context)


def profile_add(request):
    profileaddform = ProfileForm(request.POST, request.FILES)
    new_var = request.user.id
    print(new_var)
    if request.method == 'POST':

        if profileaddform.is_valid():
            print("valid")
            form = profileaddform.save(commit=False)
            form.user_id = request.user.id
            print(form.user_id)
            form.save()

            return redirect('core:profile', pk=request.user.id)

    else:
        print("load add form")
        context = {
            'profileaddform': profileaddform,
        }
        return render(request, 'core/profile_add.html', context)


def profile_update(request, pk):
    context = {}
    instance = get_object_or_404(Profile, user_id=pk)
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('core:profile', pk=pk)
    context = {
        'profileform': form,
        'instance': instance
    }

    return render(request, 'core/profile_update.html', context)

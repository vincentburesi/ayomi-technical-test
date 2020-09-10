import json
from django.contrib.auth import update_session_auth_hash
from django.http import *
from django.shortcuts import render, redirect
from accounts.forms.user_form import UserForm


def home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']

            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
                update_session_auth_hash(request, request.user)

            user.save()
            return HttpResponse()
        else:
            return HttpResponseBadRequest(json.dumps(form.errors), content_type="application/json")

    else:
        form = UserForm(initial={
            'username': user.username,
            'email': user.email,
        })
        return render(request, 'home.html', context={'userForm': form})

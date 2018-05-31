from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'home.html', context=None)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):

    return render(request, 'vegang/dashboard.html', context=None)


@login_required
def edit_profile(request):

    return render(request, 'accounts/edit_profile.html', context=None)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirm-password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Vartotojas su šiuo prisijungimo vardu jau egzistuoja!')
            return render(request, 'register/index.html')

        if password != confirmPassword:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return render(request, 'register/index.html')

        user = User.objects.create_superuser(
            username=username,
            password=password,
        )
        auth_login(request, user)
        return redirect('taxes')

    return render(request, 'register/index.html')

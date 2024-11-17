# path_to_fern_flower/views.py
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def play_game(request):
    return render(request, 'game/play.html')


# Home page
def home(request):
    return render(request, 'game/home.html')

# Register page
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created successfully for {username}! You can now log in.")
            return redirect('home')  # Redirect to the home page after successful registration
        else:
            messages.error(request, "Error creating account. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'game/register.html', {'form': form})


# Login page
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('game')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'game/login.html', {'form': form})

# Game page
def game(request):
    if request.user.is_authenticated:
        return render(request, 'game/game.html')
    else:
        return redirect('login')

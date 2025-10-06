from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Video

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'home.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return render(request, 'login.html')



@login_required    
def video_gallery(request):
    videos = Video.objects.all()
    return render(request, 'videos.html', {'videos': videos})

@login_required
def pagina1(request):
    return render(request, 'pagina1.html')

@login_required
def pagina2(request):
    return render(request, 'pagina2.html')

@login_required
def pagina3(request):
    return render(request, 'pagina3.html')

@login_required
def pagina4(request):
    return render(request, 'pagina4.html')

@login_required
def pagina5(request):
    return render(request, 'pagina5.html')

@login_required
def pagina6(request):
    return render(request, 'pagina6.html')

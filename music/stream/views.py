from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Songs

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home/')
    else:
        form = UserCreationForm()
    return render(request, 'stream/signup.html', {'form': form})

def hadu(request):
    song_list = Songs.objects.order_by('id')
    context = {'song_list': song_list}
    return render(request, 'stream/home.html', context)

def detail(request, song_id):
    s=Songs.objects.get(pk=song_id)
    url=s.song.url
    return render(request, 'stream/play.html', {'url': url})


from django.shortcuts import render, redirect
from .models import Profile, Post, FriendRequest, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            return HttpResponse("Login successful")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def home(request):
    posts = Post.objects.all()
    return render(request, 'social/home.html', {'posts': posts})

@login_required
def profile(request, user_id):
    profile = Profile.objects.get(user_id=user_id)
    return render(request, 'social/profile.html', {'profile': profile})

# def Post(request):
#     return render(request, 'social/post.html')

@login_required
def send_friend_request(request, user_id):
    to_user = User.objects.get(id=user_id)
    FriendRequest.objects.create(from_user=request.user, to_user=to_user)
    return redirect('home')

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST['content']
        image = request.FILES.get('image')
        Post.objects.create(author=request.user, content=content, image=image)
        return redirect('home')
    return render(request, 'social/create_post.html')

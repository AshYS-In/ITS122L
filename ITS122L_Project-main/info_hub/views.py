from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .models import Announcement, Event
from .forms import SignUpForm

# Create your views here.
def donate(request):
    return render(request, "info_hub/donate.html")

def contact(request):
    return render(request, "info_hub/contact.html")

def about(request):
    return render(request, "info_hub/about.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)

            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})

def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, "info_hub/announcement_list.html", {"announcements": announcements})

def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    return render(request, "info_hub/announcement_detail.html", {"announcement": announcement})

def join_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    event = get_object_or_404(Event, id=event_id)
    
    if request.user not in event.volunteers.all():
        event.volunteers.add(request.user)
    
    return redirect('event_detail', event.id)

def leave_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    event = get_object_or_404(Event, id=event_id)
    
    if request.user in event.volunteers.all():
        event.volunteers.remove(request.user)
    
    return redirect('event_detail', event.id)

def event_list(request):
    events = Event.objects.all()
    return render(request, "info_hub/event_list.html", {"events": events})

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, "info_hub/event_detail.html", {"event": event})

def index(request):
    events = Event.objects.all()
    announcements = Announcement.objects.all()
    return render(request, "info_hub/index.html", {"announcements": announcements, "events": events})

def logout_success(request):
    return render(request, "info_hub/logout_success.html")

@login_required
def profile_detail(request):
    profile = request.user.profile
    return render(request, "info_hub/profile_detail.html", {"profile": profile})

def register(request):
    pass

def volunteer(request):
    pass

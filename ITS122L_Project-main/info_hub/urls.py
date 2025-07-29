from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/logout-success/', views.logout_success, name='logout_success'),
    path("announcement/<int:id>/", views.announcement_detail, name="announcement_detail"),
    path("announcements/", views.announcement_list, name="announcement_list"),
    path("event/<int:id>/", views.event_detail, name="event_detail"),
    path('event/<int:event_id>/join/', views.join_event, name='join_event'),
    path('event/<int:event_id>/leave/', views.leave_event, name='leave_event'),
    path("events/", views.event_list, name="event_list"),
    path("donate/", views.donate),
    path("about/", views.about),
    path("profile/", views.profile_detail, name="profile"),
    path("volunteer/", views.volunteer, name="volunteer"),
    path("", views.index, name="index"),
]

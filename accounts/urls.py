from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('signup/',views.signup, name='signup'),
    path('password_change/',views.password_change, name='password_change'),
    path('profile/',views.profile, name='profile'),
    path('profile/edit/',views.profile_edit,name='profile_edit'),
]
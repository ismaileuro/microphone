from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('services', views.services, name="services"),
    path('promotion', views.promotion, name="promotion"),
    path('torronut', views.torronut, name="torronut"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('signup', views.signup, name="signup"),
    path('username-check', views.usernameCheck, name='usernameCheck'),
]

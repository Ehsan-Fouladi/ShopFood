from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("panel/<int:pk>", views.PanelView.as_view(), name="panel"),
    path("profile/<int:pk>", views.ProfileView.as_view(), name="profile"),
    path("logout/", views.LogoutView, name="logout"),
    path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]
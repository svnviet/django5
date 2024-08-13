from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login_page"),
    path("login_request/", views.login_request, name="login_request"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register_page"),
    path("recover/", views.recover, name="recover_page"),
]

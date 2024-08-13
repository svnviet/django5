import logging

from django.shortcuts import render

from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

logger = logging.getLogger(__name__)


def login_view(request):
    pass


def login_request(request):
    pass


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login_page")


def register(request):
    pass


def logout_view(request):
    pass


def recover(request):
    pass


def custom_404_view(request, exception):
    return render(request, "errors/error_500.html", status=404)


def custom_500_view(request):
    return render(request, "errors/error_500.html", status=404)

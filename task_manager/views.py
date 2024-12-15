from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    TemplateView,
    UpdateView,
)

from .mixins import ObjectContextMixin


class IndexView(TemplateView):
    template_name = "index.html"


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "form.html"
    next_page = reverse_lazy("index")
    success_message = _("You are logged in")
    extra_context = {
        "header": _("Login"),
        "button_text": _("Log in"),
    }


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You have logged out"))
        return super().dispatch(request, *args, **kwargs)


class CustomCreateView(SuccessMessageMixin, CreateView):
    template_name = "form.html"


class CustomUpdateView(SuccessMessageMixin, UpdateView):
    template_name = "form.html"


class CustomDeleteView(
        ObjectContextMixin, SuccessMessageMixin, DeleteView):
    template_name = "delete_form.html"

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
# Create your views here.
from django.views.generic import DetailView
from django_filters.views import FilterView
from task_manager.mixins import CustomLoginMixin
from task_manager.tasks.models import Task
from task_manager.views import (
    CustomCreateView,
    CustomDeleteView,
    CustomUpdateView,
)

from .filters import TaskFilter
from .forms import TaskForm
from .mixins import PermitDeleteTaskMixin


class TasksListView(CustomLoginMixin, FilterView):
    template_name = "tasks/index.html"
    model = Task
    context_object_name = "tasks"
    filterset_class = TaskFilter
    extra_context = {
        "button_text": _("Show"),
    }


class TaskCreateView(CustomLoginMixin, CustomCreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks")
    success_message = _("Task is successfully created")
    extra_context = {
        "header": _("Create task"),
        "button_text": _("Create"),
    }

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DetailTaskView(CustomLoginMixin, SuccessMessageMixin, DetailView):
    template_name = "tasks/show.html"
    model = Task


class TaskUpdateView(CustomLoginMixin, CustomUpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks")
    success_message = _("Task is successfully updated")
    extra_context = {
        "header": _("Task update"),
        "button_text": _("Update"),
    }


class TaskDeleteView(
        CustomLoginMixin, PermitDeleteTaskMixin,
        CustomDeleteView):
    model = Task
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully deleted")
    extra_context = {
        "header": _("Delete task"),
        "button_text": _("Yes, delete"),
    }

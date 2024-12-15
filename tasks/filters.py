import django_filters
import django
from django.contrib.auth.models import User

from statuses.models import Status
from labels.models import Label

from .models import Task

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all(), empty_label='---------', label='Статус')
    assigned_to = django_filters.ModelChoiceFilter(queryset=User.objects.all(), empty_label='---------', label='Исполнитель')
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all(), label='Метка')
    self_tasks = django_filters.BooleanFilter(method='filter_self_tasks', label='Только свои задачи', widget=django.forms.CheckboxInput)

    class Meta:
        model = Task
        fields = ['status', 'assigned_to', 'labels']

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

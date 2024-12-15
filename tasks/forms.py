from django import forms
from .models import Task
from labels.models import Label


class TaskForm(forms.ModelForm):
    labels = forms.ModelMultipleChoiceField(queryset=Label.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assigned_to', 'labels']

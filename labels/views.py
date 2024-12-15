from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Label
from .forms import LabelForm

class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'

class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('labels:label_list')

    def form_valid(self, form):
        messages.success(self.request, 'Метка успешно создана.')
        return super().form_valid(form)

class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('labels:label_list')

    def form_valid(self, form):
        messages.success(self.request, 'Метка успешно обновлена.')
        return super().form_valid(form)

class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/label_confirm_delete.html'
    success_url = reverse_lazy('labels:label_list')

    def delete(self, request, *args, **kwargs):
        label = self.get_object()
        # Проверяем, связана ли метка с задачами
        if label.tasks.exists():
            messages.error(self.request, 'Невозможно удалить метку, так как она связана с задачами.')
            return super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Метка успешно удалена.')
        return super().delete(request, *args, **kwargs)

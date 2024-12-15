from django.views.generic import TemplateView
from django.http import HttpResponse



class HomeView(TemplateView):
    template_name = 'index.html'


def erorr(request):
    a = None
    a.hello()  # вызов ошибки для тестирования
    return HttpResponse("Hello, world. You're at the pollapp index.")
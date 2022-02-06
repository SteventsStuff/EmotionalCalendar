from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, render
from django.views import View


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('home')


class IndexView(View):
    def get(self, request):
        return render(request, 'homepage.html')

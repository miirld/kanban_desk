from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from .models import Board
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


class CardsList(LoginRequiredMixin, ListView):
    model = Board
    template_name = 'kanban/home.html'
    context_object_name = 'boards'
    login_url = '/login/'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CardsList, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        # return News.objects.filter(is_published=True)
        return Board.objects.filter(members=self.request.user)

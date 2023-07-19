from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView
from .models import Board, Column, Card
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .forms import BoardForm, ColumnForm, CardForm
from django.http import HttpResponseRedirect


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


class CreateBoard(LoginRequiredMixin, CreateView):
    form_class = BoardForm
    template_name = "kanban/add_board.html"
    login_url = '/login/'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        form.save_m2m()
        res = super().form_valid(form)
        instance.members.add(instance.owner)
        return res


class ViewBoard(LoginRequiredMixin, ListView):
    model = Column
    template_name = "kanban/board.html"
    context_object_name = 'columns'
    login_url = '/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ViewBoard, self).get_context_data(**kwargs)
        context['board'] = Board.objects.get(pk=self.kwargs['board_id'])
        return context

    def get_queryset(self):
        # return News.objects.filter(is_published=True)
        return Column.objects.filter(board_id=self.kwargs['board_id'])


class ViewCard(LoginRequiredMixin, DetailView):
    model = Card
    context_object_name = 'card'
    template_name = 'kanban/card.html'


class CreateColumn(LoginRequiredMixin, CreateView):
    form_class = ColumnForm
    template_name = "kanban/add_column.html"
    login_url = '/login/'

    def get_form_kwargs(self):
        kwargs = super(CreateColumn, self).get_form_kwargs()
        kwargs['board_id'] = self.kwargs["board_id"]
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(CreateColumn, self).get_context_data(**kwargs)
        ctx['board'] = Board.objects.get(id=self.kwargs["board_id"])
        return ctx

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.board_id = self.kwargs['board_id']
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("view-board", kwargs={'board_id': self.kwargs['board_id']})


class CreateCard(LoginRequiredMixin, CreateView):
    form_class = CardForm
    template_name = "kanban/add_card.html"
    login_url = '/login/'

    def get_form_kwargs(self):
        kwargs = super(CreateCard, self).get_form_kwargs()
        kwargs['board_id'] = self.kwargs["board_id"]
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(CreateCard, self).get_context_data(**kwargs)
        ctx['board'] = Board.objects.get(id=self.kwargs["board_id"])
        return ctx

    def get_success_url(self):
        return reverse("view-board", kwargs={'board_id': self.kwargs['board_id']})

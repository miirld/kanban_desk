from django.contrib import admin
from .models import (Board, Column, Card)


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('owner',)
    """
    Автоматическое занесение создателя доски в ее участники при создании через админку
    """

    def save_related(self, request, form, formsets, change):
        super(BoardAdmin, self).save_related(request, form, formsets, change)
        form.instance.members.add(form.instance.owner)


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'board', 'name', 'position')
    list_display_links = ('id', 'name', 'board')
    list_filter = ('board',)


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'column', 'created_date',
                    'is_active', 'position')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('column',)


admin.site.register(Board, BoardAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Card, CardAdmin)


# Test2

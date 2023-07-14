from django.db import models

from management_site import settings


class Board(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='owned_boards',
                              verbose_name='Создатель')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='boards',
                                     verbose_name='Участники')
    name = models.CharField(max_length=50, verbose_name='Наименование')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'

    def __str__(self):
        return self.name

    """
     Автоматическое занесение создателя доски в ее участники при создании через shell
    """

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        is_new = self.pk is None
        super().save(force_insert, force_update, using, update_fields)
        if is_new:
            self.members.add(self.owner)


class Column(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='columns',
                              verbose_name='Доска')
    position = models.PositiveIntegerField(default=0, verbose_name='Позиция')

    class Meta:
        ordering = ["board", "position"]
        verbose_name = 'Столбец'
        verbose_name_plural = 'Столбцы'

    def __str__(self):
        return f"{self.name}-{self.board}"


class Card(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.CharField(max_length=300, blank=True, verbose_name='Описание')
    column = models.ForeignKey(Column, on_delete=models.CASCADE,
                               related_name='Cards',
                               verbose_name='Столбец')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Активно?')
    position = models.PositiveIntegerField(default=0, verbose_name='Позиция')
    # due_date = models.DateTimeField(verbose_name='Актуально до')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        ordering = ["position"]
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


'''
class CardActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL(),
                             null=True,
                             verbose_name='Автор')
    card = models.ForeignKey(Card, on_delete=models.CASCADE(),
                             null=True,
                             verbose_name='Карточка')
    description = models.CharField(max_length=300, null=True, verbose_name='Описание')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
'''

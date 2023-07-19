from django import forms
from .models import Board, Column, Card
from django.contrib.auth import get_user_model

# from .models import MyUser
User = get_user_model()


class BoardForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    members = forms.ModelMultipleChoiceField(label='Участники', queryset=User.objects.all(), required=False
                                             )

    class Meta:
        model = Board
        fields = ('name', 'members')


class ColumnForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    position = forms.TypedChoiceField(label='Позиция', coerce=int)

    class Meta:
        model = Column
        fields = ('name', 'position')

    def __init__(self, foo=None, *args, **kwargs):
        choices = [
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ]
        board_id = kwargs.pop('board_id')
        kwargs.update(initial={
            'board_id': board_id
        })
        super(ColumnForm, self).__init__(*args, **kwargs)
        columns = Column.objects.filter(board_id=board_id)
        for column in columns:
            choices.remove((column.position, str(column.position)))
        self.fields['position'].choices = choices


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('name', 'description', 'position')

    def __init__(self, foo=None, *args, **kwargs):
        choices = [
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
        ]
        column_pk = kwargs.pop('column_pk')
        kwargs.update(initial={
            'column_pk': column_pk
        })
        super(CardForm, self).__init__(*args, **kwargs)
        cards = Card.objects.filter(column__pk=column_pk)
        print(cards)
        for card in cards:
            choices.remove((card.position, str(card.position)))
        self.fields['position'].choices = choices

    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label='Описание',
                                  widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    position = forms.TypedChoiceField(label='Позиция', coerce=int)


class UpdateBoardForm(BoardForm):
    pass


'''
Надо реализовать через наследование
'''


class UpdateColumnForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    position = forms.TypedChoiceField(label='Позиция', coerce=int)

    class Meta:
        model = Column
        fields = ('name', 'position')

    def __init__(self, foo=None, *args, **kwargs):
        choices = [
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ]
        board_id = kwargs.pop('board_id')
        column_pk = kwargs.pop('column_pk')
        kwargs.update(initial={
            'board_id': board_id,
            'column_pk': column_pk
        })
        super(UpdateColumnForm, self).__init__(*args, **kwargs)
        columns = Column.objects.filter(board_id=board_id).exclude(pk=column_pk)
        for column in columns:
            choices.remove((column.position, str(column.position)))
        self.fields['position'].choices = choices
        self.fields['position'].help_text = f"Текущая позиция - {(Column.objects.get(pk=column_pk)).position}"


class UpdateCardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('name', 'description', 'position', 'column')

    def __init__(self, foo=None, *args, **kwargs):
        choices = [
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
        ]
        column_id = kwargs.pop('column_id')
        board_id = kwargs.pop('board_id')
        card_pk = kwargs.pop('card_pk')

        kwargs.update(initial={
            'column_id': column_id,
            'board_id': board_id,
            'card_pk': card_pk

        })

        super(UpdateCardForm, self).__init__(*args, **kwargs)
        cards = Card.objects.filter(column__id=column_id).exclude(pk=card_pk)
        for card in cards:
            print(card.position)
            choices.remove((card.position, str(card.position)))
        self.fields['position'].choices = choices
        self.fields['position'].help_text = f"Текущая позиция - {(Card.objects.get(pk=card_pk)).position}"
        self.fields['column'] = forms.ModelChoiceField(
            label='Столбец',
            queryset=Column.objects.filter(board_id=board_id),
            required=True
        )

    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label='Название',
                                  widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    position = forms.TypedChoiceField(label='Позиция', coerce=int)

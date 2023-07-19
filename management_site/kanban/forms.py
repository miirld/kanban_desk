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
            (0, '0'),
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
        fields = ('name', 'description', 'position', 'column')

    def __init__(self, foo=None, *args, **kwargs):
        choices = [
            (0, '0'),
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
        board_id = kwargs.pop('board_id')
        kwargs.update(initial={
            'board_id': board_id
        })
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['column'] = forms.ModelChoiceField(
            label='Столбец',
            queryset=Column.objects.filter(board_id=board_id),
            required=True
        )
        columns = Column.objects.filter(board_id=board_id)
        for column in columns:
            choices.remove((column.position, str(column.position)))
        self.fields['position'].choices = choices

    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label='Название',
                                  widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    position = forms.TypedChoiceField(label='Позиция', coerce=int)

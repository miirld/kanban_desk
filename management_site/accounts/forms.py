from django import forms
# from .models import MyUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField, authenticate
from django.contrib.auth import get_user_model

# from .models import MyUser
User = get_user_model()


class UserLoginForm(forms.Form):
    """
    Форма для авторизации пользователей. Включает в себя поля для
    ввода логина и пароля.
    """
    username = forms.CharField(
        label="Email",
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Введите email"
                   }
        )
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите пароль"
            }
        )
    )

    def clean_username(self):
        return self.data.get('username').lower()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username').lower()
        password = self.cleaned_data.get('password')
        current_user = authenticate(username=username, password=password)
        if not current_user:
            raise forms.ValidationError("Неверные имя пользователя или пароль")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserCreationForm(forms.ModelForm):
    """
    Форма для создания новых пользователей. Включает в себя все необходимые
    поля, в том числе и повторный пароль.
    """

    lastname = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите фамилию"
            }
        )
    )
    username = forms.CharField(
        label="Имя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите имя"
            }
        )
    )
    patronymic = forms.CharField(
        label="Отчество",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите отчество"
            }
        ),
        required=False
    )
    email = forms.CharField(
        label="Email",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите email"
            }
        )
    )
    phone = forms.CharField(
        label="Телефон",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите телефон"
            }
        )
    )
    function = forms.CharField(
        label="Должность",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите должность"
            }
        )
    )

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите пароль"
            }
        )
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Повторите пароль"}
        )
    )

    class Meta:
        model = User
        fields = ('lastname', 'username', 'patronymic', 'email')

    def clean_email(self):
        """- привести данные в нижний регистр"""
        return self.cleaned_data['email'].lower()

    def clean_password2(self):
        # Проверка. что пароли совпадают.
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли должны совпадать")
        return password2

    def save(self, commit=True):
        # Сохранение захешированных паролей
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.function = self.cleaned_data.get("function")
        user.phone = self.cleaned_data.get("phone")
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """Форма для обновления данных пользователей. Включает в себя все поля модели
     пользователь, пароль отображается в виде хеша.
    """
    lastname = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите фамилию"
            }
        )
    )
    username = forms.CharField(
        label="Имя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите имя"
            }
        )
    )
    patronymic = forms.CharField(
        label="Отчество",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите отчество"
            }
        ),
        required=False
    )
    email = forms.CharField(
        label="email",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите email"
            }
        )
    )
    phone = forms.CharField(
        label="Телефон",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите телефон"
            }
        )
    )
    function = forms.CharField(
        label="Должность",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите должность"
            }
        )
    )

    password = ReadOnlyPasswordHashField(label="Пароль")

    class Meta:
        model = User
        fields = ('lastname', 'username', 'patronymic', 'email', 'password',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

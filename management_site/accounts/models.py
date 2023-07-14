from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from .tools import hide_email


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, lastname, patronymic, phone, function, password=None):
        """
        Создает и хранит Пользователя с указанным ФИО, адресом электронной почты,
        телефоном, должностью, паролем и набором признаков: администратор организации, руководитель,
        пользователь портала, сотрудник поддержки.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), username=username, lastname=lastname,
                          patronymic=patronymic,
                          phone=phone, function=function)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username=None, lastname=None, patronymic=None, phone=None,
                         function=None):
        user = self.create_user(email, username, lastname, patronymic, phone, function, password=password)
        user.is_user = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=250, blank=True, null=True, verbose_name='Имя')
    lastname = models.CharField(max_length=250, blank=True, null=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=250, blank=True, null=True, verbose_name='Отчество')
    phone = models.CharField(max_length=250, blank=True, null=True, verbose_name='Телефон')
    function = models.CharField(max_length=250, blank=True, null=True, verbose_name='Должность')
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Активный (is_active)")
    is_admin = models.BooleanField(default=False, verbose_name="Администратор (is_admin)")
    is_staff = models.BooleanField(default=False, verbose_name="(is_staff)")
    is_user = models.BooleanField(default=True, verbose_name="Обычный пользователь (is_user)")

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['lastname', 'username', 'patronymic']

    def __str__(self):
        return f"{self.lastname} {self.username} {self.patronymic} | {hide_email(self.email)}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always

        # Есть ли у пользователя определенное разрешение?"
        # Простейший возможный ответ: Да, всегда
        return True

    def has_perms(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always

        # Есть ли у пользователя определенное разрешение?"
        # Простейший возможный ответ: Да, всегда
        return True

    def has_module_perms(self, app_label):
        "Does the user have permission s to view the app `app_label`?"
        # Simplest possible answer: Yes, always

        # Есть ли у пользователя разрешения на просмотр приложения "app_label`?"
        # Простейший возможный ответ: Да, всегда
        return True

    def get_full_name(self):
        """- получить полное имя """
        fullname = f"{self.lastname} {self.username} {self.patronymic}"
        return fullname

    def get_abbreviated_name(self):
        """- получить укороченное ФИО """
        kw = {"lastname": self.lastname if self.lastname else "",
              "username": str(self.username)[0] if self.username else "",
              "patronymic": str(self.patronymic)[0] if self.patronymic else "",
              "hide_email": f" | {hide_email(self.email)}" if hide_email(self.email) else "", }
        return "{lastname}{username}{patronymic}{hide_email}".format(**kw)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)

from django.contrib import admin

from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    save_on_top = True
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'patronymic', 'lastname', 'is_admin', 'is_active', "is_user")

    list_filter = ('is_active', 'is_admin', "is_user",)
    fieldsets = (
        (None, {'fields': (
            'username', 'lastname', 'patronymic', 'phone', 'function', 'email',
            'password',)}),
        # ('Personal info', {'fields': ('date_of_birth',)}),
        ('Роли(права)', {'fields': (
            'is_active', 'is_admin', "is_user",
        )}))

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'patronymic', 'lastname', 'phone',
                'function', 'is_active', 'is_admin',
                'password1', 'password2')}
         ),
    )
    search_fields = ('id', 'email', 'username', 'lastname', 'patronymic')
    ordering = ('email', 'username')
    filter_horizontal = ()
    '''
    def get_form(self, request, obj=None, **kwargs):
        """- изменить вид формы """
    
        if form.base_fields.get('head'):
            form.base_fields['head'].widget.attrs['style'] = 'width: 100em;'
            form.base_fields['head'].label = ''

        if form.base_fields.get('recipients'):
            form.base_fields['recipients'].widget.attrs['style'] = 'width: 100em;'
            form.base_fields['recipients'].label = ''

    return form
    '''


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

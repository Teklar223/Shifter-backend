from django.contrib import admin
from django.apps import apps
from .models import CustomUser as User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
'''
class CustomUserAdmin(admin.ModelAdmin):
    exclude = tuple() # ('password',) # TODO: Exclude password
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_superuser',)
    readonly_fields = tuple() # ('email',) # TODO: email is readonly
'''

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'
        exclude = ('username',)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)

    def get_fields(self):
        fields = super().get_fields()
        fields.remove('username')
        return fields

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user 

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    exclude = ('username',)
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_superuser',)
    readonly_fields = () #('email',)

    def get_fieldsets(self, request, obj=None):
        if not obj:  # Creating a new user
            return (
                (None, {'fields': ('email', 'password1', 'password2')}),
                ('Permissions', {'fields': ('is_superuser',)}),
            )
        return super().get_fieldsets(request, obj)
    
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            self.form = self.add_form
        else:
            self.form = self.form
        return super().get_form(request, obj, **kwargs)


all_models = apps.get_models()
for model in all_models:
    try:
        if model.__name__ == User.__name__:
            admin.site.register(model, CustomUserAdmin)
        else:    
            admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
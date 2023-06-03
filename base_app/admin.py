from django.contrib import admin
from django.apps import apps
from .models import CustomUser as User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
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

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_superuser',)
    readonly_fields = ('email',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not obj:  # Creating a new user
            fieldsets += (
                (None, {'fields': ('email',)}),
            )
        return fieldsets


all_models = apps.get_models()
for model in all_models:
    try:
        if model.__name__ == User.__name__:
            admin.site.register(model, CustomUserAdmin)
        else:    
            admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
from django.contrib import admin
from django.apps import apps
from .models import CustomUser as User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

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
    ordering = ('username',)
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'permission_scope')}),
        ('Relationships', {'fields': ('company_id', 'team_id', 'role_id')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:  # Creating a new user
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


all_models = apps.get_models()
for model in all_models:
    try:
        if model.__name__ == User.__name__:
            admin.site.register(model, CustomUserAdmin)
        else:    
            admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
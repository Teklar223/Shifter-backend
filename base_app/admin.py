from django.contrib import admin
from django.apps import apps
from .models import CustomUser as User

class CustomUserAdmin(admin.ModelAdmin):
    exclude = tuple() # ('password',) # TODO: Exclude password
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_superuser',)
    readonly_fields = tuple() # ('email',) # TODO: email is readonly

all_models = apps.get_models()
for model in all_models:
    try:
        if model.__name__ == User.__name__:
            admin.site.register(model, CustomUserAdmin)
        else:    
            admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
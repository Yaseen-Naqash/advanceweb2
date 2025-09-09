from django.contrib import admin
from .models import Person, Blog
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# admin.site.register(Person)
# admin.site.register(Blog)




class BlogAdmin(admin.ModelAdmin):

    # list view settings
    list_display_links = ['created_at']
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author']
    # search_fields = ['title', 'body']
    list_editable = ['title', 'author']
    fieldsets = [
        (
            None,
            {
                "fields": ["title", "body"],
            },
        ),
        (
            "users",
            {
                "classes": ["wide"],
                "fields": ["author", "readers"],
            },
        ),
    ]
 
    # details view settings
    readonly_fields = ['title']
    # autocomplete_fields = ['author']
    

    pass
admin.site.register(Blog, BlogAdmin)



admin.site.register(Person)









from django.contrib import admin
from .models import BlogPost
admin.site.register(BlogPost)


# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title',)  # Show title in the list view
#     fields = ('title', 'content')  # Fields to show in the edit form

# admin.site.register(BlogPost, BlogPostAdmin)

from django.contrib import admin
from blogging.models import Post, Category
# Register your models here.

class CatergoriesInline(admin.TabularInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CatergoriesInline,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category,CategoryAdmin)
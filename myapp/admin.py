from django.contrib import admin
from .models import posts, Category



class postsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at','content']
    search_fields = ['title', 'content']
    list_filter = ['created_at', 'category']



# Register your models here.
admin.site.register(posts, postsAdmin)
admin.site.register(Category)
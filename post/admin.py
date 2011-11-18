from django.contrib import admin 
from shdnbi.post.models import Category, Post  

class CategoryAdmin(admin.ModelAdmin): 
    prepopulated_fields = { 'slug': ['title'] }
	
class PostAdmin(admin.ModelAdmin): 
    prepopulated_fields = { 'slug': ['title'] }
	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
from django.contrib import admin
from .models import BlogPost, Announcement, Comment, SiteSettings, PageContent

# Personnalisation de l'affichage des articles de blog dans l'admin

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at' ,'updated_at')

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_editable = ('status',)
    ordering = ['-created_at']

# Personnalisation de l'affichage des annonces dans l'admin
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'message')
    ordering = ['-created_at']
    list_editable = ('is_active',)

# Personnalisation de l'affichage des commentaires dans l'admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog_post', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'name')
    search_fields = ('content', 'blog_post__title')
    ordering = ['-created_at']

# Enregistrer les modèles dans l'admin
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Comment, CommentAdmin)


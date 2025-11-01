from django.contrib import admin
from .models import Project, IntroVideo, Profile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'tech_stack', 'created_at')
    list_filter = ('created_at', 'tech_stack')
    search_fields = ('title', 'description', 'tech_stack')
    list_editable = ('position',)
    ordering = ('position', '-created_at')

@admin.register(IntroVideo)
class IntroVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'uploaded_at')
    list_filter = ('is_active', 'uploaded_at')
    readonly_fields = ('uploaded_at',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'about_me')
        }),
        ('Skills', {
            'fields': ('frontend_skills', 'backend_skills', 'database_skills', 'tools_skills')
        }),
        ('Portfolio & Contact', {
            'fields': ('portfolio_description', 'contact_description', 'email', 'linkedin', 'github')
        }),
        ('Media', {
            'fields': ('profile_image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

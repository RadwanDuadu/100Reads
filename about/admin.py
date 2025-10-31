from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, Contact

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)

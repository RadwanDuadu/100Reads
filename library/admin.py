from django.contrib import admin
from .models import Book, Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug')
    search_fields = ['title', 'content']
    list_filter = ( 'published_year',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

admin.site.register(Review)

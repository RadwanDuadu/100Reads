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

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("book", "author", "rating", "approved", "created_on")
    list_filter = ("approved", "created_on", "rating", "book")
    search_fields = ("body", "author__username", "book__title")
    save_as = False  # <- ensure cloning button is gone
    list_editable = ("approved",)

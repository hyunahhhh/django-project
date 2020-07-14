from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
# models.py 에서 만든 테이블 반영

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
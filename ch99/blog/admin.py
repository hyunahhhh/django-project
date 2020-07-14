from django.contrib import admin
from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 이거 컬럼들만 보여지게!
    list_display = ('id', 'title', 'modify_dt', 'content', 'create_dt', 'description')
    # admin 사이트에서 필터 걸 수 있는 옵션
    list_filter = ('modify_dt',)
    # 탐색 기능
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

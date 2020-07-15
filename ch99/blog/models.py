from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):

    # 테이블에 담길 column들
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)  # 날짜 역순(최신글이 위에 보여지게)

    def __str__(self):
        return self.title

    # get_absolute_url()메소드 - 정의된 객체를 지칭하는 URL을 반환
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    # get_previous()메소드 - 메소드 내에서 장고의 내장 함수인 get_previous_by_modify_dt()를 호출
    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()
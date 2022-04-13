from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class PostModel(models.Model):
    """Модель поста"""

    title = models.CharField(
                            max_length=120,
                            verbose_name="Заголовок статьи"
                            )
    content = models.TextField("Содержание поста")
    author = models.ForeignKey(
                               User,
                               on_delete=models.CASCADE,
                               related_name="posts",
                               verbose_name="Автор",
                               )
    created = models.DateTimeField(
                                  auto_now_add=True,
                                  verbose_name="Дата создания"
                                  )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class CommentModel(MPTTModel):
    """Модель комментария"""
    post = models.ForeignKey(
                            PostModel,
                            on_delete=models.CASCADE,
                            related_name="comments",
                            )
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children')
    
    author_name = models.CharField('Автор отзыва', max_length=50, default='Гость')
    text = models.TextField("Текст комментария")
    pub_date = models.DateTimeField(
                                   "Дата создания комментария",
                                   auto_now_add=True,
                                   )

    def save(self, *args, **kwargs):
        if parent.level == 3:
            raise ValueError("Достигнута максимальная вложенность!")
        

    def __str__(self):
        return f"Комментарий от пользователя {self.author_name} level {self.parent}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    class MPTTMeta:
        order_insertion_by = ['text']

    def __unicode__(self):
        return self.author_name


    

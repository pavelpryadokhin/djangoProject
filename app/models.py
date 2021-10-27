from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Articles(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    body = models.TextField(verbose_name="Текст")
    timestamp=models.DateTimeField('Дата создания',auto_now=False, auto_now_add=True )
    updated=models.DateTimeField('Дата обновления',auto_now=True, auto_now_add=False )
    status=(('r1','Роман'),('p','Поэма'),('r2','Рассказ'),('s','Стих'))
    status= models.CharField('Жанр',choices=status,max_length=2,default='r1')
    post_like = models.IntegerField('Лайк', default = 0)
    post_dislike = models.IntegerField('Дизлайк', default = 0)

    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'
        db_table='posts'#задали название в БД
        ordering=['-title']#порядок

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:post_detail',kwargs={'pk':self.id})

class Like(models.Model):
    LIKE_OR_DISLAKE_CHOICES = (
        ("LIKE", "like"),
        ("DISLIKE", "dislike"),
        (None, "None")
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    for_post = models.ForeignKey(Articles, on_delete = models.CASCADE)
    like_or_dislike = models.CharField(max_length=7,
                                       choices=LIKE_OR_DISLAKE_CHOICES,
                                       default=None)

class Comments(models.Model):
    comment_text=models.TextField('Комментарий')
    comment_article=models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья', related_name='comments')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Автор комментария', blank = True, null = True)
    timepublish=models.DateTimeField('Дата пуликации',auto_now=False, auto_now_add=True, blank=True, null=True )
    active=models.BooleanField(default=True)


    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'
        db_table='comments'


    def __str__(self):
        return self.comment_text


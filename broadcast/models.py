from django.db import models


class CategoryModel(models.Model):
    category_title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title


class NewsModel(models.Model):
    news_title = models.CharField(max_length=200)
    content = models.TextField(help_text='Описание новости')
    news_image = models.FileField(upload_to='news_image')
    news_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

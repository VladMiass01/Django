from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='Скоро тут будет рецепт...')
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
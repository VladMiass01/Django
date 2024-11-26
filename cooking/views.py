from django.views.generic import ListView, DetailView
from  django.db.models import Q
from .models import Category, Post


class Index(ListView):
    model = Post
    extra_context = {'title': 'Главная страница'}
    context_object_name = 'posts'
    template_name = 'index.html'


class ArticleByCategory(Index):


    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['pk'])


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context


class PostDetail(DetailView):
    model = Post
    template_name = '_article_detail.html'


    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        post = Post.objects.get(pk=self.kwargs['pk'])
        context['title'] = post.title
        return context


class SearchResult(Index):


    def get_queryset(self):
        word = self.request.GET.get('q')
        posts = Post.objects.filter(Q(title__icontains=word) | Q(content__icontains=word))
        return posts

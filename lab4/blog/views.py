from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Article, Category

class HomePageView(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_articles'] = Article.objects.filter(featured=True)[:3]
        context['categories'] = Category.objects.all()
        return context


class ArticleListView(ListView):
    model = Article
    template_name = "blog/articles_list.html"
    context_object_name = "articles"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"


class CategoryArticlesView(ListView):
    template_name = "blog/category_articles.html"
    context_object_name = "articles"
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Article.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        return context

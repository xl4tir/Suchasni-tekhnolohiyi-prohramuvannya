from django.test import TestCase
from django.urls import reverse
from .models import Category, Article

class BlogTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Технології", slug="tehnologii")
        self.article = Article.objects.create(
            title="Штучний інтелект 2050",
            description="Спроба змоделювати майбутнє",
            category=self.category,
            featured=True
        )

    def test_article_str(self):
        self.assertEqual(str(self.article), "Штучний інтелект 2050")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Технології")

    def test_article_detail_view(self):
        url = reverse("article_detail", args=[self.article.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.article.title)

    def test_category_articles_view(self):
        url = reverse("category_articles", args=[self.category.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.category.name)

    def test_homepage_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/home.html")

    def test_articles_list_view(self):
        response = self.client.get(reverse("articles"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/articles_list.html")

    def test_article_get_absolute_url(self):
        self.assertEqual(self.article.get_absolute_url(), f"/article/{self.article.slug}/")

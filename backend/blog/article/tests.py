from django.test import TestCase
from django.urls import reverse
from .models import Article
from django.utils import timezone
# Create your tests here.

# *****************************************************************************************ARTICLE*************************************


class HomePageTests(TestCase):
    def test_home_page_status_code_by_adress(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_page_status_code_by_view_name(self):
        response = self.client.get(reverse('article:article_list_view'))
        self.assertEquals(response.status_code, 200)


class DetailPageTests(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title="Testing article title",
            text="Testing article text",
            postedDate=timezone.now()
        )

    def test_detail_article_page_status_code_by_adress(self):
        response = self.client.get('/' + str(self.article.id))
        self.assertEquals(response.status_code, 200)

    def test_detail_article_page_status_code_by_view_name(self):
        response = self.client.get(
            reverse('article:article_detail_view', kwargs={"pk": self.article.pk}))
        self.assertEquals(response.status_code, 200)

# *****************************************************************************************API*************************************


class ApiListPageTests(TestCase):
    def test_list_of_articles_api_page_status_code_by_adress(self):
        response = self.client.get('/api/')
        self.assertEquals(response.status_code, 200)

    def test_list_of_articles_api_page_status_code_by_viewname(self):
        response = self.client.get(reverse('api:list-view'))
        self.assertEquals(response.status_code, 200)


class ApiDetailPageTests(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title="Testing article title",
            text="Testing article text",
            postedDate=timezone.now()
        )

    def test_details_of_article_api_page_status_code_by_adress(self):
        response = self.client.get("/api/" + str(self.article.pk))
        self.assertEquals(response.status_code, 200)

    def test_details_of_article_api_page_status_code_by_view_name(self):
        response = self.client.get(
            reverse("api:detail-view", kwargs={"pk": self.article.pk}))
        self.assertEquals(response.status_code, 200)

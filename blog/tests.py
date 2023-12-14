from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
        username="testuser", email="test@email.com", password="secret"
        )
        cls.post = Post.objects.create(
        title="A dianosour",
        meta_text = 'About dianosour',
        body="It was a big dianosour",
        author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A dianosour")
        self.assertEqual(self.post.body, "It was a big dianosour")
        self.assertEqual(self.post.meta_text, "About dianosour")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "1-A dianosour")
        self.assertEqual(self.post.get_absolute_url(), "/blog/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 200)
        
    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About dianosour")
        self.assertTemplateUsed(response, "blog/home.html")
        
    def test_post_detailview(self):
        response = self.client.get(reverse("blog_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/blog/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A dianosour")
        self.assertTemplateUsed(response, "blog/post_detail.html")
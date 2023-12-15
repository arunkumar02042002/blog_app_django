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
        description = 'About dianosour',
        body="It was a big dianosour",
        author=cls.user,
        )
    
    # Testing The Post Model
    def test_post_model(self):
        self.assertEqual(self.post.title, "A dianosour")
        self.assertEqual(self.post.body, "It was a big dianosour")
        self.assertEqual(self.post.description, "About dianosour")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "1-A dianosour")
        self.assertEqual(self.post.get_absolute_url(), "/blog/1/")
        
    # Testing the correct location of list view
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # Testing whether the correct location of detail view
    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/blog/1/")
        self.assertEqual(response.status_code, 200)
    
    # Testing the list view
    def test_blog_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About dianosour")
        self.assertTemplateUsed(response, "blog/home.html")
    
    # Testing detail view
    def test_blog_detailview(self):
        response = self.client.get(reverse("blog_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/blog/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A dianosour")
        self.assertTemplateUsed(response, "blog/blog_detail.html")

    # Testing Create View
    def test_blog_createview(self):
        response = self.client.post(
        reverse("blog_new"),
        {
        "title": "New title",
        "description": 'New description',
        "body": "New text",
        "author": self.user.id,
        },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().description, "New description")
        self.assertEqual(Post.objects.last().body, "New text")

    # Testing Update View
    def test_blog_updateview(self):
        response = self.client.post(
            reverse("blog_edit", args='1'),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")

    # Testing Delete View
    def test_blog_deleteview(self):
        response = self.client.post(reverse("blog_delete", args="1"))
        self.assertEqual(response.status_code, 302)

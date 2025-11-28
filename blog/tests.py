from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Category, Tag

class BlogE2ETest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Technology')
        self.tag = Tag.objects.create(name='Python')
        self.post = Post.objects.create(
            title='Test Post',
            author=self.user,
            content='This is a test post content.',
            status='published',
            category=self.category
        )
        self.post.tags.add(self.tag)

    def test_blog_list_page(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_list.html')
        self.assertContains(response, 'Test Post')

    def test_blog_detail_page(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_detail.html')
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post content.')

    def test_draft_post_not_visible(self):
        draft_post = Post.objects.create(
            title='Draft Post',
            author=self.user,
            content='Draft content',
            status='draft',
            category=self.category
        )
        response = self.client.get(reverse('blog_list'))
        self.assertNotContains(response, 'Draft Post')

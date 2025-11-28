from django.test import TestCase, Client
from django.urls import reverse
from .models import Project

class PagesE2ETest(TestCase):
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title="Test Project",
            description="Test Description",
            image="project_images/test.jpg",
            link="http://example.com",
            order=1
        )

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "Hello, I'm Mansii")

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, "About Me")

    def test_portfolio_page(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio.html')
        self.assertContains(response, "Test Project")

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertContains(response, "Get in Touch")

from django.test import TestCase
from django.urls import reverse
from .models import posts, Category

class PostModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_unique_slug_generation(self):
        post1 = posts.objects.create(title='Test Post', content='Some content.', category=self.category)
        post2 = posts.objects.create(title='Test Post', content='Some more content.', category=self.category)

        self.assertEqual(post1.slug, 'test-post')
        self.assertEqual(post2.slug, 'test-post-1')

class ViewsTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.post = posts.objects.create(title='Test Post', content='Some content.', category=self.category)

    def test_detail_view_with_valid_slug(self):
        response = self.client.get(reverse('myapp:Detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_detail_view_with_invalid_slug(self):
        response = self.client.get(reverse('myapp:Detail', kwargs={'slug': 'invalid-slug'}))
        self.assertEqual(response.status_code, 404)
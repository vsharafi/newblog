from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='user')
        cls.post1 = Post.objects.create(title='post title', text='post text', author=user, status='pub')


    def test_posts_list_url(self):
        response = self.client.get('/blog/')
        response_name = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_name.status_code, 200)
    
    def test_posts_list_content(self):
        response = self.client.get('/blog/')
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_content(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.text)

    
    def test_status_404_if_id_not_found(self):
        response = self.client.get('/blog/100/')
        self.assertEqual(response.status_code, 404)

    def test_post_list_templates(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/posts_list.html')
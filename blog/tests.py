from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user')
        cls.post1 = Post.objects.create(title='post title', text='post text', author=cls.user, status='pub')
        cls.post2 = Post.objects.create(title='post title 2', text='post text 2', author=cls.user, status='drf')


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
        
    
    def test_draft_not_show_in_list(self):
        response = self.client.get('/blog/')
        self.assertNotContains(response, self.post2.text)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_add'), {'title':'title', 'text':'text', 'author': self.user.id, 'status':'pub'})
        response1 = self.client.get('/blog/')
        self.assertContains(response1, 'text')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'title')
        self.assertEqual(Post.objects.last().author, self.user)

    def test_post_model_str(self):
        self.assertEqual(str(self.post1), self.post1.title)


    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post1.id]), {'title':'title', 'text':'text', 'author': self.user.id, 'status':'pub'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.get(id=self.post1.id).title, 'title')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)
        response1 = self.client.get('/blog/')
        self.assertNotContains(response1, 'post title')
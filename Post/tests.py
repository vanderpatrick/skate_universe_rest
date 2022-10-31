from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewsTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='socrates', password='mocrates')

    def test_can_list_posts(self):
        socrates = User.objects.get(username='socrates')
        Post.objects.create(author=socrates, title='a new title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='socrates', password='mocrates')
        response = self.client.post('/posts/', {'title': 'a new title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cant_post(self):
        response = self.client.post('/posts/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Post.objects.create(
            author=adam, title='a title', content='adams content'
        )
        Post.objects.create(
            author=brian, title='another title', content='brians content'
        )

    def test_can_retrive(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['a title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
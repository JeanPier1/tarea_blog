from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        p = Blog('Test','jefe')
        self.assertEqual('Test',p.title)
        self.assertEqual('jefe', p.author)
        self.assertEqual([], p.posts)

    def test_repr(self):
        b = Blog('Test','Test Author')
        b2 = Blog('My Day', 'Fred')

        self.assertEqual(b.__repr__(),'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(),'My Day by Fred (0 posts)')

    def test_repr_multiple_posts(self):
        b= Blog('Test','Test Author')
        b.posts = ['test']

        b2 = Blog('My Day', 'Freed')
        b2.posts = ['test','another']

        self.assertEqual(b.__repr__(),'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Freed (2 posts)')
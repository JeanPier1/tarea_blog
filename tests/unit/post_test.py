from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content', '12-12-12')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)
        self.assertEqual('12-12-12', p.fecha)

    def test_json(self):
        p = Post('Test', 'Test Content', '12-12-12')
        expected = {'title': 'Test',
                    'content': 'Test Content',
                    'date': '12-12-12'}
        self.assertDictEqual(expected, p.json())

    def test_repor(self):
        p = Post('Test', 'Test Content', '2012-12-12 00:00:00')
        p2 = Post('Pruebita', 'Contenido dicernido', '2013-12-13 00:00:00')
        self.assertEqual(
            p.__repr__(), 'Test by Test Content the 2012-12-12 00:00:00')
        self.assertEqual(
            p2.__repr__(), 'Pruebita by Contenido dicernido the 2013-12-13 00:00:00')

    def test_verificar(self):
        p = Post('Test', 'Test Content', '2013-12-13 00:00:00')
        self.assertEqual(
            p.__repr__(), 'Test by Test Content the 2013-12-13 00:00:00')

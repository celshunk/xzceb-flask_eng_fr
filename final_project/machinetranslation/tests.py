import unittest

from translator import englishToFrench, frenchToEnglish

class TestMyModule(unittest.TestCase):
    def test_englishToFrench(self):
        text='Hello'
        self.assertIsNotNone(text)
        self.assertEqual(englishToFrench(text),'Bonjour')

class TestMyModule(unittest.TestCase):
    def test_frenchToEnglish(self):
        text='Bonjour'
        self.assertIsNotNone(text)
        self.assertEqual(frenchToEnglish(text),'Hello')


if __name__=='__main__':
    unittest.main()

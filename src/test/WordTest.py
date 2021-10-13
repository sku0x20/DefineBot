import unittest

from Word import Word


class WordTest(unittest.TestCase):

    def test_valueObject(self):
        word1a = Word("word1", "meaning1")
        word1b = Word("word1", "meaning1")
        word2 = Word("word2", "meaning2")
        self.assertEqual(word1a, word1a)
        self.assertEqual(word1a, word1b)
        self.assertNotEqual(word1a, word2)

    def test_hash(self):
        word1a = Word("word1", "meaning1")
        word1b = Word("word1", "meaning1")
        word2 = Word("word2", "meaning2")
        self.assertEqual(word1a.__hash__(), word1a.__hash__())
        self.assertEqual(word1a.__hash__(), word1b.__hash__())
        self.assertNotEqual(word1a.__hash__(), word2.__hash__())


if __name__ == '__main__':
    unittest.main()

import unittest

from Word import Definition, Word, Homograph


class DefinitionTest(unittest.TestCase):

    def test_valueObject(self):
        definition1a = Definition("word1", "meaning1", "some example")
        definition1b = Definition("word1", "meaning1", "some example")
        definition2 = Definition("word2", "meaning2", "some example")
        self.assertEqual(definition1a, definition1a)
        self.assertEqual(definition1a, definition1b)
        self.assertNotEqual(definition1a, definition2)

    def test_hash(self):
        definition1a = Definition("noun", "meaning1", "some example")
        definition1b = Definition("noun", "meaning1", "some example")
        definition2 = Definition("adjective", "meaning2", "some example")
        self.assertEqual(definition1a.__hash__(), definition1a.__hash__())
        self.assertEqual(definition1a.__hash__(), definition1b.__hash__())
        self.assertNotEqual(definition1a.__hash__(), definition2.__hash__())


class WordTest(unittest.TestCase):

    def test_valueObject(self):
        word1a = Word("word1", [Homograph("", [Definition("noun", "meaning1", "")])])
        word1b = Word("word1", [Homograph("", [Definition("noun", "meaning1", "")])])
        word2 = Word("word2", [Homograph("", [Definition("noun", "meaning1", "")])])
        self.assertEqual(word1a, word1a)
        self.assertEqual(word1a, word1b)
        self.assertNotEqual(word1a, word2)

    def test_hash(self):
        word1a = Word("word1", [Homograph("", [Definition("noun", "meaning1", "")])])
        word1b = Word("word1", [Homograph("", [Definition("noun", "meaning1", "")])])
        word2 = Word("word2", [Homograph("", [Definition("noun", "meaning1", "")])])
        self.assertEqual(word1a.__hash__(), word1a.__hash__())
        self.assertEqual(word1a.__hash__(), word1b.__hash__())
        self.assertNotEqual(word1a.__hash__(), word2.__hash__())


if __name__ == '__main__':
    unittest.main()

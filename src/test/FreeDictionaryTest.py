import unittest

from httpretty import httpretty

import JsonSamples
from FreeDictionary import FreeDictionary


class FreeDictionaryTest(unittest.TestCase):

    def setUp(self) -> None:
        httpretty.enable(verbose=True, allow_net_connect=False)

    def tearDown(self) -> None:
        httpretty.disable()
        httpretty.reset()

    def test_queryWord_SingleMeaning(self):
        httpretty.register_uri(httpretty.GET, FreeDictionary.API.format(word="anonymous"),
                               body=JsonSamples.anonymousResponse)
        wordLookup = FreeDictionary.queryWord("anonymous")
        self.assertEqual(word.word, "anonymous")
        # self.assertEqual(word.definition, "(of a person) not identified by name; of unknown name.")
        # self.assertEqual(word.example, "(of a person) not identified by name; of unknown name.")
        # self.assertEqual(word.partOfSpeech, "adjective")

    def test_queryWord_MultiMeaning(self):
        pass


if __name__ == '__main__':
    unittest.main()

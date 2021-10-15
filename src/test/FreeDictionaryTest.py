import unittest

from httpretty import httpretty

import JsonSamples
from FreeDictionary import FreeDictionary
from Word import Homograph, Definition


class FreeDictionaryTest(unittest.TestCase):

    def setUp(self) -> None:
        httpretty.enable(verbose=True, allow_net_connect=False)

    def tearDown(self) -> None:
        httpretty.disable()
        httpretty.reset()

    def test_queryWord_SingleMeaning(self):
        httpretty.register_uri(httpretty.GET, FreeDictionary.API.format(word="anonymous"),
                               body=JsonSamples.anonymousResponse)
        word = FreeDictionary.queryWord("anonymous")
        self.assertEqual(word.word, "anonymous")
        self.assertEqual(len(word.homographs), 1)
        homograph = word.homographs[0]
        expectedHomograph = Homograph(
            "late 16th century: via late Latin from Greek anōnumos ‘nameless’ (from an- ‘without’ + onoma ‘name’) + "
            "-ous.",
            [
                Definition(
                    "adjective",
                    "(of a person) not identified by name; of unknown name.",
                    "the donor's wish to remain anonymous"
                )
            ])
        self.assertEqual(homograph, expectedHomograph)

    def test_queryWord_MultiMeaning(self):
        pass


if __name__ == '__main__':
    unittest.main()

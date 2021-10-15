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
            {"adjective": [
                Definition(
                    "adjective",
                    "(of a person) not identified by name; of unknown name.",
                    "the donor's wish to remain anonymous"
                )
            ]})
        self.assertEqual(homograph, expectedHomograph)

    # def test_queryWord_MultiMeaning(self):
    #     httpretty.register_uri(httpretty.GET, FreeDictionary.API.format(word="test"),
    #                            body=JsonSamples.testResponse)
    #     word = FreeDictionary.queryWord("test")
    #     self.assertEqual(word.word, "test")
    #     self.assertEqual(len(word.homographs), 2)
    #     firstHomograph = word.homographs[0]
    #     expectedHomograph = Homograph(
    #         "late 16th century: via late Latin from Greek anōnumos ‘nameless’ (from an- ‘without’ + onoma ‘name’) + "
    #         "-ous.",
    #         {"adjective": [
    #             Definition(
    #                 "adjective",
    #                 "(of a person) not identified by name; of unknown name.",
    #                 "the donor's wish to remain anonymous"
    #             )
    #         ]})
    #     self.assertEqual(homograph, expectedHomograph)

    def _firstTestHomograph(self):
        return Homograph(
            "late Middle English (denoting a cupel used to treat gold or silver alloys or ore): via Old French from "
            "Latin testu, testum ‘earthen pot’, variant of testa ‘jug, shell’. Compare with test2. The verb dates "
            "from the early 17th century. ",
            {}[
                Definition(
                    "noun",
                    "a procedure intended to establish the quality, performance, or reliability of something, "
                    "especially before it is taken into widespread use.",
                    "both countries carried out nuclear tests in May"
                )
            ]
        )


if __name__ == '__main__':
    unittest.main()

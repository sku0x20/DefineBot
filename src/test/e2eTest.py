import os
import unittest

import httpretty

import Constants
import JsonSamples
import TestUtils
from app import app


class EndToEndTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        os.environ["TEST"] = "1"
        cls.client = app.test_client()

    def setUp(self) -> None:
        httpretty.enable(verbose=True, allow_net_connect=False)

    def tearDown(self) -> None:
        httpretty.disable()
        httpretty.reset()

    def test_ping(self):
        rv = self.client.post(
            "/interactions/",
            data=TestUtils.createPingBody(),
            headers={"Content-Type": "application/json"}
        )
        response = rv.json
        self.assertDictEqual({"type": 1}, response)

    def test_highFive(self):
        rv = self.client.post(
            "/interactions/",
            data=TestUtils.stringFromJsonSample(JsonSamples.hiveFiveRequest),
            headers={"Content-Type": "application/json"}
        )
        response = rv.json
        self.assertDictEqual({
            "type": 4,
            "data": {
                "tts": False,
                "content": "High Five <@678704423321638412801>",
                "embeds": [],
                "allowed_mentions": {"parse": ["users"]}
            }
        }, response)

    def test_singleMeaningWord(self):
        httpretty.register_uri(httpretty.GET, Constants.FREE_DICTIONARY_API.format(word="anonymous"),
                               body=JsonSamples.anonymousResponse)
        rv = self.client.post(
            "/interactions/",
            data=TestUtils.stringFromJsonSample(JsonSamples.defineRequest)
                .replace("wordToSearch", "anonymous"),
            headers={"Content-Type": "application/json"}
        )
        response = rv.json
        self.assertDictEqual({
            "type": 4,
            "data": {
                "tts": False,
                "content": "*anonymous*: (of a person) not identified by name; of unknown name.",
                "embeds": [],
                "allowed_mentions": {"parse": []}
            }
        }, response)

    # def test_singleMeaningWord(self):
    #     httpretty.enable(verbose=True, allow_net_connect=False)
    #     httpretty.register_uri(httpretty.GET, "https://api.dictionaryapi.dev/api/v2/entries/en/anonymous",
    #                            body=anonymousResponse)
    #
    #     word = getWordMeaning("anonymous")
    #     self.assertEqual(word.word, "anonymous")
    #     self.assertEqual(word.definition, "(of a person) not identified by name; of unknown name.")
    #
    #     httpretty.disable()
    #     httpretty.reset()
    #
    # def test_NoMeaningFound(self):
    #     pass

    # @unittest.skip
    # def test_multiMeaningWord(self):
    #     # will do it later on
    #     # https://api.dictionaryapi.dev/api/v2/entries/en/cricket
    #     self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

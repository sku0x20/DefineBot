import os
import re
import unittest

import httpretty

import Constant
import TestUtils
from app import app


class EndToEndTests(unittest.TestCase):

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

    # def test_CommandHighFive(self):
    #     rv = self.client.post(
    #         "/interactions/",
    #         data=createHighFiveRequest(),
    #         headers={"Content-Type": "application/json"}
    #     )
    #     response = rv.json
    #     self.assertDictEqual({"type": 1}, response)

    # def test_singleMeaningWord(self):
    # httpretty.register_uri(httpretty.GET, Constant.FREE_DICTIONARY_API.format(word="anonymous"),
    #                        body=anonymousResponse)
    # rv = self.client.get(
    #     "/interactions/",
    #     data=pingRequest.format(
    #         applicationId="1234567890",
    #         requestId="09123231234",
    #         requestToken="abcDefghiJkl01234"
    #     )
    # )
    # response = rv.json
    # self.assertEqual("<p>App is live</p>", body)

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

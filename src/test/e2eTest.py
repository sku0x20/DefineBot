import os
import unittest

import httpretty

from FreeDictionary import FreeDictionary
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
        httpretty.register_uri(httpretty.GET, FreeDictionary.API.format(word="anonymous"),
                               body=JsonSamples.anonymousResponse)
        rv = self.client.post(
            "/interactions/",
            data=TestUtils.stringFromJsonSample(JsonSamples.defineRequest)
                .replace("wordToSearch", "anonymous"),
            headers={"Content-Type": "application/json"}
        )
        response = rv.json
        content = (
            "1. anonymous \n"
            "  a. adjective; \n"
            "    - (of a person) not identified by name; of unknown name. \n"
            "      e.g. the donor's wish to remain anonymous "
        )
        self.assertEqual(response["data"]["content"], content)
        self.assertDictEqual({
            "type": 4,
            "data": {
                "tts": False,
                "content": content,
                "embeds": [],
                "allowed_mentions": {"parse": []}
            }
        }, response)

    def test_MultiMeaningWord(self):
        httpretty.register_uri(httpretty.GET, FreeDictionary.API.format(word="test"),
                               body=JsonSamples.testResponse)
        rv = self.client.post(
            "/interactions/",
            data=TestUtils.stringFromJsonSample(JsonSamples.defineRequest)
                .replace("wordToSearch", "test"),
            headers={"Content-Type": "application/json"}
        )
        response = rv.json
        content = self._getWordTestContent()
        self.assertEqual(response["data"]["content"], content)
        self.assertDictEqual({
            "type": 4,
            "data": {
                "tts": False,
                "content": content,
                "embeds": [],
                "allowed_mentions": {"parse": []}
            }
        }, response)

    # def test_NoMeaningFound(self):
    #     pass

    def _getWordTestContent(self):
        return (
            "1. test \n"
            "  a. noun; \n"
            "    - a procedure intended to establish the quality, performance, or reliability of something, especially before it is taken into widespread use. \n"
            "      e.g. both countries carried out nuclear tests in May \n"
            "    - short for Test match. \n"
            "      e.g. the first Test against New Zealand \n"
            "    - a movable hearth in a reverberating furnace, used for separating gold or silver from lead. \n"
            "      e.g.  \n"
            "  b. verb; \n"
            "    - take measures to check the quality, performance, or reliability of (something), especially before putting it into widespread use or practice. \n"
            "      e.g. this range has not been tested on animals \n"
            "2. test \n"
            "  a. noun; \n"
            "    - the shell or integument of some invertebrates and protozoans, especially the chalky shell of a foraminiferan or the tough outer layer of a tunicate. \n"
            "      e.g.  "
        )


if __name__ == '__main__':
    unittest.main()

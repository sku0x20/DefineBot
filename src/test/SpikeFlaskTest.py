import os
import unittest

from flask import Flask, request

from DiscordUtils import verify

spikeTestApp = Flask(__name__)


@spikeTestApp.route("/")
def root():
    if os.environ["TEST"] != "1":
        # cannot find any other good way to disable verify for tests
        verify(request)
    return "<p>App is live</p>"


class SpikeFlaskTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        os.environ["TEST"] = "1"

    def setUp(self) -> None:
        self.client = spikeTestApp.test_client()

    def tearDown(self) -> None:
        # i cannot find a good way to close the client
        # self.client.__exit__()
        pass

    def test_spikeMessage(self):
        rv = self.client.get("/")
        body = rv.data.decode("utf-8")
        self.assertEqual("<p>App is live</p>", body)


if __name__ == "__main__":
    unittest.main()
    # It is important to remember that the test class has been derived from unittest. Hence, we need to include main
    # and invoke unittest.main() in it. To execute the test case, we use
    # https://dzone.com/articles/python-unit-testing-one-time-initialization

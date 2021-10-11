import unittest

import httpretty
import requests

anonymousResponse = '''
[
   {
      "word":"anonymous",
      "phonetic":"əˈnɒnɪməs",
      "phonetics":[
         {
            "text":"əˈnɒnɪməs",
            "audio":"//ssl.gstatic.com/dictionary/static/sounds/20200429/anonymous--_gb_1.mp3"
         }
      ],
      "origin":"late 16th century: via late Latin from Greek anōnumos ‘nameless’ (from an- ‘without’ + onoma ‘name’) + -ous.",
      "meanings":[
         {
            "partOfSpeech":"adjective",
            "definitions":[
               {
                  "definition":"(of a person) not identified by name; of unknown name.",
                  "example":"the donor's wish to remain anonymous",
                  "synonyms":[
                     "unnamed",
                     "of unknown name",
                     "nameless",
                     "incognito",
                     "unidentified",
                     "unknown",
                     "unspecified",
                     "undesignated",
                     "unacknowledged",
                     "mystery",
                     "unsung",
                     "innominate",
                     "unsigned",
                     "unattributed",
                     "unattested",
                     "uncredited"
                  ],
                  "antonyms":[
                     "known",
                     "identified",
                     "signed"
                  ]
               }
            ]
         }
      ]
   }
]
'''


class EndToEndTests(unittest.TestCase):

    def test_singleMeaningWord(self):
        httpretty.enable(verbose=True, allow_net_connect=False)
        httpretty.register_uri(httpretty.GET, "https://api.dictionaryapi.dev/api/v2/entries/en/anonymous",
                               body=anonymousResponse)

        response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/anonymous")
        self.assertEqual(response.json(), anonymousResponse)

        httpretty.disable()
        httpretty.reset()

    @unittest.skip
    def test_multiMeaningWord(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

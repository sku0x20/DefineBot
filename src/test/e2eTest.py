import unittest
import httpretty

from main import getWordMeaning


class EndToEndTests(unittest.TestCase):

    def test_flaskSingleMeaningWord(self):
        pass

    def test_singleMeaningWord(self):
        httpretty.enable(verbose=True, allow_net_connect=False)
        httpretty.register_uri(httpretty.GET, "https://api.dictionaryapi.dev/api/v2/entries/en/anonymous",
                               body=anonymousResponse)

        word = getWordMeaning("anonymous")
        self.assertEqual(word.word, "anonymous")
        self.assertEqual(word.definition, "(of a person) not identified by name; of unknown name.")

        httpretty.disable()
        httpretty.reset()

    def test_NoMeaningFound(self):
        pass

    @unittest.skip
    def test_multiMeaningWord(self):
        # will do it later on
        # https://api.dictionaryapi.dev/api/v2/entries/en/cricket
        self.assertEqual(True, False)  # add assertion here


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

if __name__ == '__main__':
    unittest.main()

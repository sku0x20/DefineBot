from typing import Final

import requests

from Word import Word, Homograph, Definition


class FreeDictionary:
    API: Final = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    @classmethod
    def queryWord(cls, wordStr) -> Word:
        response = requests.get(cls.API.format(word=wordStr))
        return cls._parseWordFromResponse(response.json())

    # methods stating with _ should be considered private
    @classmethod
    def _parseWordFromResponse(cls, jsonResponse) -> Word:
        wordStr = jsonResponse[0]["word"]
        homographs = []
        for i in range(len(jsonResponse)):
            definitions = []
            # for
            print(jsonResponse[i])
        definition = jsonResponse[0]["meanings"][0]["definitions"][0]["definition"]
        return Word("test", [Homograph("", [Definition("test", "test", "test")])])

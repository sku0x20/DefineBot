from typing import Final

import requests

from Word import Word


class FreeDictionary:
    API: Final = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    @classmethod
    def queryWord(cls, wordStr) -> Word:
        response = requests.get(cls.API.format(word=wordStr))
        return cls._parseWordFromResponse(response.json())

    @classmethod
    def _parseWordFromResponse(cls, jsonResponse) -> Word:
        word = jsonResponse[0]["word"]
        definition = jsonResponse[0]["meanings"][0]["definitions"][0]["definition"]
        return Word(word, definition)

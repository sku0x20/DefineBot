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
        for homographJsonObject in jsonResponse:
            definitions = {}
            for meaningJsonObject in homographJsonObject["meanings"]:
                currentPartOfSpeech: str = meaningJsonObject["partOfSpeech"]
                definitions[currentPartOfSpeech] = []
                for definitionJsonObject in meaningJsonObject["definitions"]:
                    definition = definitionJsonObject["definition"]
                    example = definitionJsonObject.get("example", "")
                    definitions[currentPartOfSpeech].append(Definition(currentPartOfSpeech, definition, example))
            origin = homographJsonObject["origin"]
            homographs.append(Homograph(origin, definitions))
        return Word(wordStr, homographs)

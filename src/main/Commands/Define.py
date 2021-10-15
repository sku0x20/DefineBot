from typing import Final

from Commands.DiscordCommand import DiscordCommand
from FreeDictionary import FreeDictionary
from Word import Word


class Define(DiscordCommand):
    COMMAND_NAME: Final = "define"

    def execute(self, jsonRequest) -> dict:
        wordStr = jsonRequest["data"]["options"][0]["value"]
        word = FreeDictionary.queryWord(wordStr)
        return ({
            "type": 4,
            "data": {
                "tts": False,
                "content": self._formatWord(word),
                "embeds": [],
                "allowed_mentions": {"parse": []}
            }
        })

    @staticmethod
    def _formatWord(word: Word):
        count = 1
        formattedString = f"  {word.word} \n"
        for homograph in word.homographs:
            formattedString += f"{count}. "
            for key, value in homograph.definitions.items():
                for definition in value:
                    formattedString += f"{definition.partOfSpeech}; {definition.definition} \n"
                    formattedString += f"   e.g. {definition.example}"
            count += 1
        return formattedString

from typing import Final

from Commands.DiscordCommand import DiscordCommand
from main import getWordMeaning


class Define(DiscordCommand):
    COMMAND_NAME: Final = "define"

    def execute(self, jsonRequest) -> dict:
        wordStr = jsonRequest["data"]["options"][0]["value"]
        word = getWordMeaning(wordStr)
        return ({
            "type": 4,
            "data": {
                "tts": False,
                "content": f"*{word.word}*: {word.definition}",
                "embeds": [],
                "allowed_mentions": {"parse": []}
            }
        })

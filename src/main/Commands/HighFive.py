from typing import Final

from Commands.DiscordCommand import DiscordCommand


class HighFive(DiscordCommand):
    COMMAND_NAME: Final = "High Five"

    def execute(self, jsonRequest) -> dict:
        userFrom = jsonRequest["member"]["user"]["id"]
        userTo = jsonRequest["data"]["target_id"]
        return ({
            "type": 4,
            "data": {
                "tts": False,
                "content": f"High Five <@{userTo}>",
                "embeds": [],
                "allowed_mentions": {"parse": ["users"]}
            }
        })

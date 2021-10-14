from abc import abstractmethod, ABC
from typing import Final


class DiscordCommand(ABC):
    # i could use property here, but let it be as it is for now
    COMMAND_NAME = "Should be implemented"

    # this does not adhere to Command Query Separation
    # but as Kent Beck(if i remember correctly) said, "world is not that binary"
    # maybe this design can be improved maybe I can use collecting parameter.
    # but for now YAGANI
    @abstractmethod
    def execute(self, jsonRequest) -> dict:
        pass

    @classmethod
    def isCommand(cls, commandName) -> bool:
        return cls.COMMAND_NAME == commandName

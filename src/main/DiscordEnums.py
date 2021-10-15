from enum import IntEnum


class InteractionType(IntEnum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3


# todo: nobody using this enum
class ApplicationCommandType(IntEnum):
    CHAT_INPUT = 1,
    USER = 2,
    MESSAGE = 3

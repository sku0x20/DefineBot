from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Word:
    word: str
    origin: str
    definitions: List["Definition"]

    # just for sake; we are only checking weather two word strings match,
    # if they do, we return true, since a word should be unique in itself
    # it can have different definition/meanings but it's unique in itself
    # I should however throw exception when same word have different definitions
    # but for sake simplicity gonna ignore it for now...
    def __eq__(self, other: object) -> bool:
        if other is self:  # reference to same object
            return True
        if not isinstance(other, Word):
            return False
        return other.word == self.word

    # since word should be unique in itself
    def __hash__(self):
        return self.word.__hash__()


@dataclass(frozen=True)
class Definition:  # also called meaning
    partOfSpeech: str
    definition: str
    example: str

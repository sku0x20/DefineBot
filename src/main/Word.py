from dataclasses import dataclass


@dataclass(frozen=True)
class Word:
    word: str
    definition: str

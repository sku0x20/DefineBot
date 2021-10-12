from dataclasses import dataclass


@dataclass(frozen=True)
class Word:
    word: str
    meaning: str

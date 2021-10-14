from dataclasses import dataclass
from typing import List

from Word import Word


@dataclass(frozen=True)
class WordLookup:
    words: List[Word]

from dataclasses import dataclass


@dataclass(slots=True)
class Keyword:

    phrase: str

    frequency: int

    pages: int

    score: float = 0.0
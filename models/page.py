from dataclasses import dataclass, field


@dataclass(slots=True)
class Page:

    url: str

    title: str = ""

    description: str = ""

    canonical: str = ""

    h1: list[str] = field(default_factory=list)

    h2: list[str] = field(default_factory=list)

    text: str = ""

    language: str = ""

    word_count: int = 0
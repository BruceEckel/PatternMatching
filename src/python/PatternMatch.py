# https://github.com/BruceEckel/PatternMatching/src/python
# PatternMatch.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Bicycle:
    id: str

@dataclass(frozen=True)
class Glider:
    size: int

@dataclass(frozen=True)
class Surfboard:
    weight: float

@dataclass(frozen=True)
class Skis:
    length: int

def exhaustive(t: Bicycle | Glider | Surfboard) -> str:
    match t:
        case Bicycle() as b: return f"Bicycle {b.id}"
        case Glider() as g: return f"Glider {g.size}"
        case Surfboard() as s: return f"Surfboard {s.weight}"
        case _: return f"Unrecognized transport {t}"

[print(exhaustive(it)) for it in
    [Bicycle("Bob"), Glider(65), Surfboard(6.4), Skis(72)]]

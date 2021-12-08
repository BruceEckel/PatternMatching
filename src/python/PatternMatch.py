# 3. PatternMatch.py
# Disjoint classes passed as a type union, using pattern matching
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
    def additional(self) -> str: return "additional!"

def show(t: Bicycle | Glider | Surfboard) -> str:
    match t:
        case Bicycle() as b: return f"Bicycle {b.id}"
        case Glider() as g: return f"Glider {g.size}"
        case Surfboard() as s: return f"Surfboard {s.weight}"
        case Skis() as s: return f"Skis {s.length} {s.additional()}"
        case _: return f"Unrecognized transport {t}"

[print(show(it)) for it in
    [Bicycle("Bob"), Glider(65), Surfboard(6.4), Skis(72)]]

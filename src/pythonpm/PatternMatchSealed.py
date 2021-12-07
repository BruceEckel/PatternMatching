# https://github.com/BruceEckel/PatternMatching
# PatternMatchSealed.py
from dataclasses import dataclass

# @sealed
class Transport:
    pass

@dataclass(frozen=True)
class Bicycle(Transport):
    id: str

@dataclass(frozen=True)
class Glider(Transport):
    size: int

@dataclass(frozen=True)
class Surfboard(Transport):
    weight: float

@dataclass(frozen=True)
class Skis(Transport):
    length: int

def exhaustive(t: Transport) -> str:
    match t:
        case Bicycle() as b: return f"Bicycle {b.id}"
        case Glider() as g: return f"Glider {g.size}"
        case Surfboard() as s: return f"Surfboard {s.weight}"
        case _: return f"Unrecognized transport {t}"

[print(exhaustive(it)) for it in
   [Bicycle("Bob"), Glider(65), Surfboard(6.4), Skis(72)]]

# 4. PatternMatchSealed.py
# Sealed class hierarchy, parameter expanded to type union
from dataclasses import dataclass

# @sealed # Proposed in PEP 622
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
    # (t: Bicycle | Glider | Surfboard | Skis)
    match t:
        case Bicycle() as b: return f"Bicycle {b.id}"
        case Glider() as g: return f"Glider {g.size}"
        case Surfboard() as s: return f"Surfboard {s.weight}"
        case Skis() as s: return f"Skis {s.length}"

[print(exhaustive(it)) for it in
   [Bicycle("Bob"), Glider(65), Surfboard(6.4), Skis(72)]]

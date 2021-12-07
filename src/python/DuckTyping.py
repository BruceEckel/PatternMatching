# https://github.com/BruceEckel/PatternMatching/src/python
# DuckTyping.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Bicycle:
    id: str
    def display(self) -> str: return f"Bicycle {self.id}"

@dataclass(frozen=True)
class Glider:
    size: int
    def display(self) -> str: return f"Glider {self.size}"

@dataclass(frozen=True)
class Surfboard:
    weight: float
    def display(self) -> str: return f"Glider {self.weight}"

@dataclass(frozen=True)
class Skis:
    length: int
    def display(self) -> str: return f"Glider {self.length}"

def exhaustive(t) -> str:
    return t.display()

[print(exhaustive(it)) for it in
   [Bicycle("Bob"), Glider(65), Surfboard(6.4), Skis(72)]]

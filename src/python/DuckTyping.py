# 2. DuckTyping.py
# Disjoint classes containing a common operation
from dataclasses import dataclass
from typing import Any

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
    def display(self) -> str: return f"Surfboard {self.weight}"

@dataclass(frozen=True)
class Skis:
    length: int
    def display(self) -> str: return f"Skis {self.length}"

def exhaustive(t: Any) -> str:
    return t.display()

[print(exhaustive(it)) for it in
   [Bicycle("Bob"), Glider(65), Surfboard(6.4), Skis(72)]]

# https://github.com/BruceEckel/PatternMatching
# Inheritance.py
from dataclasses import dataclass

class Transport:
    def display(self) -> str: pass

@dataclass(frozen=True)
class Bicycle(Transport):
    id: str
    def display(self) -> str: return f"Bicycle {self.id}"

@dataclass(frozen=True)
class Glider(Transport):
    size: int
    def display(self) -> str: return f"Glider {self.size}"

@dataclass(frozen=True)
class Surfboard(Transport):
    weight: float
    def display(self) -> str: return f"Surfboard {self.weight}"

@dataclass(frozen=True)
class Skis(Transport):
    length: int
    def display(self) -> str: return f"Skis {self.length}"

def exhaustive(t: Transport) -> str:
    return t.display()

[print(exhaustive(it)) for it in
   [Bicycle("Bob"), Glider(65), Surfboard(6.4), Skis(72)]]

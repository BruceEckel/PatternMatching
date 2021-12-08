# 1. Inheritance.py
# Classical inheritance with an abstract base class and data classes
from dataclasses import dataclass
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
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
    def additional(self) -> str: return "not available from base"

def show(t: Transport) -> str: return t.display()

[print(show(it)) for it in
    [Bicycle("Bob"), Glider(65), Surfboard(6.4), Skis(72)]]

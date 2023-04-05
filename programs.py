from dataclasses import dataclass
from abc import ABC


@dataclass
class Program(ABC):
    """Represents the abstract base class of the washing programs"""

    name: str
    price: int


@dataclass
class PreWashing(Program):
    name: str = "Pre-washing"
    price: int = 1.5


@dataclass
class PressureWashing(Program):
    name: str = "Pressure washing"
    price: int = 2.5


@dataclass
class ActiveFoam(Program):
    name: str = "Active foaming"
    price: int = 2


@dataclass
class Rinsing(Program):
    name: str = "Rinsing"
    price: int = 1

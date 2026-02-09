from abc import abstractmethod
from typing import Dict, Any

from interface import ISerializable


class Vehicle(ISerializable):
    """Clase Base Abstracta. No se pueden crear 'Vehículos' genéricos."""

    def __init__(self, brand: str, model: str) -> None:
        # ENCAPSULAMIENTO: Atributos privados con doble guion bajo
        self.__brand = brand
        self.__model = model

    # --- GETTERS (Estilo Python con decoradores) ---
    @property
    def brand(self) -> str:
        return self.__brand

    @property
    def model(self) -> str:
        return self.__model

    @abstractmethod
    def move(self) -> str:
        """Cada hijo debe explicar cómo se mueve."""
        pass



from typing import Dict, Any

from vehicle import Vehicle


class Boat(Vehicle):
    """Clase Concreta: Barco"""

    def __init__(self, brand: str, model: str, is_sailboat: bool) -> None:
        super().__init__(brand, model)
        self.__is_sailboat = is_sailboat

    def move(self) -> str:
        tipo = "Velero" if self.__is_sailboat else "Lancha"
        return f"⚓ El {tipo} {self.brand} navega por el agua."

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "type": "Boat",
            "is_sailboat": self.__is_sailboat
        })
        return data
from typing import Dict, Any

from vehicle import Vehicle


class Airplane(Vehicle):
    """Clase Concreta: Avión"""

    def __init__(self, brand: str, model: str, max_altitude: float) -> None:
        super().__init__(brand, model)
        self.__max_altitude = max_altitude

    def move(self) -> str:
        return f"✈️  El {self.brand} vuela a {self.__max_altitude} pies."

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "type": "Airplane",
            "max_altitude": self.__max_altitude
        })
        return data

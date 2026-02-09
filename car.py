from vehicle import Vehicle


class Car(Vehicle):
    """Clase Concreta: Auto"""

    def __init__(self, brand: str, model: str, num_doors: int) -> None:
        super().__init__(brand, model)
        self.__num_doors = num_doors

    def move(self) -> str:
        return f"🚗 El {self.brand} conduce por la carretera."

    # POLIMORFISMO en la serialización
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            "type": "Car",  # Etiqueta vital para saber qué clase es al cargar
            "num_doors": self.__num_doors
        })
        return data
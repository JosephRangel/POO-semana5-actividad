import json
import os
from typing import List

from airplane import Airplane
from boat import Boat
from car import Car
from vehicle import Vehicle


class FleetManager:
    """Se encarga de guardar y cargar la lista de vehículos."""

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def save_fleet(self, fleet: List[Vehicle]) -> None:
        try:
            # List comprehension: Convertimos cada objeto a dict
            data = [vehicle.to_dict() for vehicle in fleet]
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"✅ Datos guardados en {self.filename}")
        except IOError as e:
            print(f"❌ Error al guardar: {e}")

    def load_fleet(self) -> List[Vehicle]:
        if not os.path.exists(self.filename):
            return []

        fleet = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data_list = json.load(f)

            for item in data_list:
                # FACTORY PATTERN (Simplificado)
                # Reconstruimos el objeto según su etiqueta "type"
                if item["type"] == "Car":
                    obj = Car(item["brand"], item["model"], item["num_doors"])
                elif item["type"] == "Airplane":
                    obj = Airplane(item["brand"], item["model"], item["max_altitude"])
                elif item["type"] == "Boat":
                    obj = Boat(item["brand"], item["model"], item["is_sailboat"])
                else:
                    continue  # Tipo desconocido, lo saltamos

                fleet.append(obj)

            return fleet
        except (json.JSONDecodeError, KeyError):
            return []

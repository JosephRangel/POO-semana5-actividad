import os
from typing import List

from airplane import Airplane
from boat import Boat
from car import Car
from data import FleetManager
from vehicle import Vehicle


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display():
    manager = FleetManager("cesun_garage.json")
    fleet: List[Vehicle] = manager.load_fleet()
    while True:
        clear_screen()
        print("=== SISTEMA DE REGISTRO VEHICULAR (CESUN) ===")
        print(f"Vehículos en garaje: {len(fleet)}")
        print("1. Registrar Auto")
        print("2. Registrar Avión")
        print("3. Registrar Barco")
        print("4. Ver flota (Polimorfismo)")
        print("5. Guardar y Salir")

        option = input("\nSelecciona una opción: ")

        if option in ["1", "2", "3"]:
            brand = input("Marca: ")
            model = input("Modelo: ")

            if option == "1":
                doors = int(input("Número de puertas: "))
                fleet.append(Car(brand, model, doors))

            elif option == "2":
                alt = float(input("Altitud máxima (pies): "))
                fleet.append(Airplane(brand, model, alt))

            elif option == "3":
                is_sail = input("¿Es velero? (s/n): ").lower() == 's'
                fleet.append(Boat(brand, model, is_sail))

            print("✅ ¡Vehículo agregado!")
            input("Enter para continuar...")

        elif option == "4":
            print("\n--- REPORTE DE FLOTA ---")
            if not fleet:
                print("El garaje está vacío.")
            else:
                for idx, v in enumerate(fleet, 1):
                    # Aquí ocurre la magia del POLIMORFISMO:
                    # Llamamos a .move() y cada objeto sabe qué hacer
                    print(f"{idx}. {v.brand} {v.model} -> {v.move()}")
            input("\nEnter para continuar...")

        elif option == "5":
            manager.save_fleet(fleet)
            print("¡Hasta la próxima clase!")
            break
from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle
class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Добавлено: {vehicle.get_info()}")

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            print(f"Удалено: {vehicle.get_info()}")
        else:
            print("Этого транспорта нет в гараже")

    def show_all(self):
        if not self.vehicles:
            print("Гараж пуст")
            return
        print(f"В гараже {len(self.vehicles)} транспортных средств:")
        for vehicle in self.vehicles:
            print(f"  - {vehicle.get_info()}")

    def count_by_type(self):
        counts = {}
        for vehicle in self.vehicles:
            type_name = type(vehicle).__name__
            counts[type_name] = counts.get(type_name, 0) + 1
        return counts
from models.vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors=doors
    def move(self):
            return "Автомобиль движется по дороге"
    def get_info(self):
        return f"автомобиль:{self.brand} {self.model} ({self.year}) дверей:{self.doors},скорость:{self.speed} км/ч"
    def __str__(self):
        return f"автомобиль:{self.brand} {self.model} ({self.year}) дверей:{self.doors},скорость:{self.speed} км/ч"
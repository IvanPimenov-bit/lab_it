from models.vehicle import Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar=has_sidecar
    def move(self):
        return "Мотоцикл движется по дороге"
    def get_info(self):
        sidecar = "с коляской" if self.has_sidecar else "без коляски"
        return f"Мотоцикл: {self.brand} {self.model} ({self.year}), {sidecar}, скорость:{self.speed} км/ч"
    
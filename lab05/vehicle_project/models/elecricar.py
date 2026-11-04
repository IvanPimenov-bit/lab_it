from models.car import  Vehicle
class Electricar(Vehicle):
    def __init__(self, brand, model, year, battery, range_km):
        super().__init__(brand, model, year)
        self.battery=battery
        self.range_km=range_km
    def move(self):
        return "Электрокар движется по трассе"
    def get_info(self):
        return f"электрокар: {self.brand} {self.model} ({self.year}), Заряд батареи: {self.battery}%, запас хода: {self.range_km}км, скорость: {self.speed} км/ч" 
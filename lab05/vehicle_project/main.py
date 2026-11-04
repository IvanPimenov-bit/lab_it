from models.vehicle import Vehicle
from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle
from models.elecricar import Electricar
from garage import Garage
def main():
    truck1=Truck("KAMAZ","PRO",2000,1500)
    motorcycle1=Motorcycle("Subaru","f200",2015,True)
    car1=Car("Toyta","turbo",2014,"4")
    car2=Car("Ferraru","red",2000,"2")
    tesla=Electricar("Tesla","X",2022,100,50)
    vehicles=[car1, car2, truck1, motorcycle1,tesla]
    car1.speed=10
    car2.speed=40
    tesla.accelerate(66)
    truck1.accelerate(50)
    truck1.brake(20)
    motorcycle1.accelerate(100)
    garage = Garage()
    garage.add_vehicle(car1)
    garage.add_vehicle(truck1)
    garage.add_vehicle(motorcycle1)
    garage.show_all()
    garage.remove_vehicle(car2)     
    garage.remove_vehicle(truck1)
    garage.show_all()
    garage.add_vehicle(tesla)  
    garage.show_all()
    try:
        Vehicle("Toyota", "Camry", 2024)
    except TypeError as e:
        print("Ошибка:", e)
    for vehicle in vehicles:
        print(vehicle.move())
        print(vehicle.get_info())
        print()
if __name__ == "__main__":
    main()

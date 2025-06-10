from Car import car

Car_1 = car("Chevy", "Corvette", "2021", "blue")
Car_2 = car("Toyota", "Yaris", "2011", "green")

print(Car_1.make)
print(Car_1.model)
print(Car_1.year)
print(Car_1.color)


Car_1.drive()
Car_1.stop()
class House:
    def __init__(self, number_of_floors = 0):
        self.number_of_floors = number_of_floors


    def set_new_number_of_floors(self, floors):
        self.number_of_floors = floors
        print('изменённое количество этажей', self.number_of_floors)


duplex = House(2)
print("список атрибутов duplex", duplex.__dict__)

villa = House()
print("список атрибутов villa", villa.__dict__)

print(duplex.number_of_floors)
duplex.set_new_number_of_floors(6)
print(duplex.number_of_floors)










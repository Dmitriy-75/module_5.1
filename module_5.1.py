class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor >  self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)

house_JR = House('Жигулина Роща',16)
house_GM = House('Город Мира',9)
house_JR.go_to(5)
house_GM.go_to(10)
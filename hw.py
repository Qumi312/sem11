class Animal:
    def __init__(self, name):
        self.name = name



class AnimalFactory(Animal):
    def create_animal(type, name, weight):

        if type == 'Bird':
            return Bird(name, weight)
        elif type == 'Fish':
            return Fish(name, weight)
        elif type == 'Mammal':
            return Mammal(name, weight)
        else:
            raise(ValueError('Недопустимый тип животного'))

class Bird(Animal):
    def __init__(self):
        super().__init__('Bird')

    def __init__(self, name: str, wingspan: float | int):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name: str, max_depth: float | int):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Средневодная рыба'


class Mammal(Animal):
    def __init__(self, name: str, weight: float | int):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        return 'Обычный'


if __name__ == '__main__':
    # b = Bird('Bird1', 2.5)
    # f = Fish('Fish1', 2.5)
    # m = Mammal('Mammal1', 2.5)
    animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
    animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
    animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
    # print(f'{b.wing_length()}')
    # print(f'{f.depth()}')
    # print(f'{m.category()}')1
    print(animal1.wing_length())
    print(animal2.depth())
    print(animal3.category())

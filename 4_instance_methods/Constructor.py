# Напишите определение класса Constructor
class Constructor:
    def add_atribute(self, name, value):
        setattr(self, name, value)

    def display(self):
        print(f'{self.__dict__}')


# Ниже код для проверки класса Constructor

obj1 = Constructor()
assert obj1.__dict__ == {}
obj1.display()
obj1.add_atribute('color', 'red')
assert obj1.color == 'red'
obj1.add_atribute('width', 20)
assert obj1.width == 20
obj1.display()

obj2 = Constructor()
obj2.display()
obj2.add_atribute('height', 100)
assert obj2.height == 100
obj2.display()

obj3 = Constructor()
obj3.display()
obj3.add_atribute('a', 100)
obj3.add_atribute('b', 300)
obj3.add_atribute('c', 200)
obj3.add_atribute('b', 1)
assert obj3.__dict__ == {'a': 100, 'b': 1, 'c': 200}
obj3.display()

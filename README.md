# OB04_Solid
## Branch_3_Lesson_Cod
### Part_3
Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)

# Lesson_Cod
class Bird():
    def __Init__(self, name):
        self.name = name

    def fly(self):
        print("Птица летает")

class Ping(Bird):
    pass

p= Ping("Сара")

p.fly()

Пример с ошибкой в логике - пингвин не умеет летать

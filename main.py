# Lesson_Cod
class Bird():
    def Fly(self):
        print("Эта птица летает")


class Duck(Bird):
    def Fly(self):
        print("Эта утка летает быстро")

def fly_in_the_sky(animal):
    animal.fly()


b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)



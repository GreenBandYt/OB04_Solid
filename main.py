import random
import pickle
from abc import ABC, abstractmethod

# Абстрактный класс Оружие
class Weapon(ABC):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    @abstractmethod
    def attack(self):
        pass

# Класс Меч, наследующий от Оружия
class Sword(Weapon):
    def __init__(self):
        super().__init__("Меч", 10)

    def attack(self):
        return "наносит удар мечом"

# Класс Лук, наследующий от Оружия
class Bow(Weapon):
    def __init__(self):
        super().__init__("Лук", 5)

    def attack(self):
        return "стреляет из лука"

# Класс Кулак, наследующий от Оружия
class Hand(Weapon):
    def __init__(self):
        super().__init__("Кулак", 3)

    def attack(self):
        return "наносит удар рукой"

# Класс Боец
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    # Метод для выбора случайного оружия
    def choose_random_weapon(self):
        self.weapon = random.choice([Sword(), Bow(), Hand()])

    # Метод для атаки
    def fight(self):
        # Перед каждой атакой выбираем случайное оружие
        self.choose_random_weapon()
        return f"{self.name} {self.weapon.attack()}."

# Класс Монстр
class Monster:
    def __init__(self, name, health):
        # Конструктор класса Монстр принимает имя и здоровье
        self.name = name
        self.health = health
        self.is_alive = True

    def die(self):
        self.is_alive = False
        return f"Монстр {self.name} побежден!"

# Функция битвы
def battle(fighter, monster):
    while monster.is_alive:
        print(fighter.fight())
        # Уменьшаем здоровье монстра
        monster.health -= fighter.weapon.damage
        print(f"Здоровье монстра: {monster.health}")

        # Генерируем случайное увеличение силы оружия
        weapon_upgrade = random.randint(0, 5)
        fighter.weapon.damage += weapon_upgrade
        print(f"Сила оружия увеличена на {weapon_upgrade} и равна {fighter.weapon.damage}.")

        if monster.health <= 0:
            print(monster.die())
            print(f"Боец {fighter.name} победил.")
        else:
            print("Монстр жив.")

# Функция для загрузки бойцов из файла
def load_fighters(filename="fighters.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []

# Функция для сохранения бойцов в файл
def save_fighters(fighters, filename="fighters.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(fighters, f)

# Главная функция
def main():
    fighters = load_fighters()
    fighter = None

    while True:
        print("\n1. Добавить нового бойца")
        print("2. Выбрать бойца из списка")
        print("3. Начать битву")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            fighter_name = input("Имя бойца: ")
            fighter = Fighter(fighter_name)
            fighters.append(fighter)
            print(f"Боец {fighter_name} добавлен.")

        elif choice == '2':
            if not fighters:
                print("Список бойцов пуст.")
                continue

            print("Список бойцов:")
            for i, fighter in enumerate(fighters):
                print(f"{i + 1}. {fighter.name}")

            index = int(input("Выберите номер бойца: ")) - 1
            if 0 <= index < len(fighters):
                fighter = fighters[index]
                print(f"Выбран боец {fighter.name}.")
            else:
                print("Неверный номер бойца.")

        elif choice == '3':
            if not fighter:
                print("Сначала выберите или добавьте бойца.")
                continue

            monster_name = input("Имя монстра: ")
            monster_health = int(input("Здоровье монстра: "))
            monster = Monster(monster_name, monster_health)
            battle(fighter, monster)

        elif choice == '4':
            save_fighters(fighters)
            print("Бойцы сохранены. Выход из игры.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

# Проверяем, что запуск происходит из главного модуля
if __name__ == "__main__":
    main()

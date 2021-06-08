from os import system
from random import randint


class Weapon:
    def __init__(self, name: str, damage: int, life: int):
        self.__name = name
        self.__life = life
        self.__damage = damage

    def hit(self, opponent):
        opponent.life = opponent.life - self.__damage
        self.__damage -= 1

    @property
    def name(self):
        return self.__name

    @property
    def damage(self):
        return self.__damage


class Character:
    def __init__(self, life: int, weapon: Weapon):
        self.__weapon = weapon
        self.__life = life

    def shoot(self, opponent):
        self.__weapon.hit(opponent)

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, new_life):
        self.__life = new_life

    @property
    def weapon_info(self):
        return self.__weapon.name

    @property
    def damage(self):
        return self.__weapon.damage


class Enemy(Character):
    pass


class Player(Character):

    def __init__(self, name: str, life: int, weapon: Weapon):
        Character.__init__(self, life, weapon)
        self.__name = name

    @property
    def name(self):
        return self.__name


def main():
    enemies = list()
    for i in range(10):
        enemies.append(Enemy(randint(30, 50), Weapon("Knife", randint(10, 20), 35)))

    player = Player("PL1", 170, Weapon("Sword", 45, 50))
    while True:
        system("cls")
        print(f"Player : {player.name} Life : {player.life} Weapon {player.weapon_info} Damage : {player.damage}")
        print("*" * 50)
        for num, i in enumerate(enemies):
            print(f"Num : {num} Enemy Life : {i.life} Enemy Damage {i.damage} Enemy Weapon {i.weapon_info}")

        print("*" * 50)
        hit = int(input("Enemy to attack : "))
        enemy = enemies[hit]
        player.shoot(enemy)

        if enemy.life <= 0:
            enemies.remove(enemy)
            if not enemies:
                print("Game Over You Won")
                break
        # Enemy Attack
        if enemies:
            enemies[randint(0, len(enemies) - 1)].shoot(player)
            if player.life <= 0:
                print("Game Over You Lost")
                break


if __name__ == '__main__':
    main()

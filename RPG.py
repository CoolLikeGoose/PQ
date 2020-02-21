import random
import time


class Attack:
    @staticmethod
    def attack_target(person, target):
        hit = random.choice(person.atk_chance)
        if hit:
            target.hp -= person.dmg
            print(f'{person.name} hit the {target.name} and deal {person.dmg}, now {target.name} has {target.hp} hp')
        else:
            print(f'{person.name} has missed')

        time.sleep(1)

    @staticmethod
    def attack_chance(percent):
        att = [False for i in range(10)]
        p = percent // 10
        for i in range(p):
            att[i] = True
        return att

    @staticmethod
    def fight(*persons):
        while 1:
            if persons[0].hp <= 0:
                print(f'{persons[1].name} win!')
                break
            Attack.attack_target(persons[0], persons[1])
            if persons[1].hp <= 0:
                print(f'{persons[0].name} win!')
                break
            Attack.attack_target(persons[1], persons[0])


class Warrior:
    def __init__(self, name):
        self.hp = 100
        self.dmg = 20
        self.name = name
        self.atk_chance = Attack.attack_chance(80)


bob = Warrior('Bob')
joe = Warrior('Joe')
Attack.fight(bob, joe)
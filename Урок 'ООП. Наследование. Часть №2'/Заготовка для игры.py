class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        pass


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x = delta_x
        self.pos_y = delta_y

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return (self.pos_x, self.pos_y)


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.weapon = weapon
        self.hp = hp

    def hit(self, target):
        if isinstance(target, MainHero):
            pass
        else:
            return 'Могу ударить только Главного героя'


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.name = name
        self.hp = hp
        self.weapon = []

    def hit(self, target):
        if len(self.weapon) == 0:
            return "Я безоружен"
        else:
            if isinstance(target, BaseCharacter):
                target.hp -= self.weapon_now.damage
            else:
                return "Могу ударить только Врага"

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            if len(self.weapon) == 0:
                self.weapon_now = weapon
                self.weapon.append(weapon)
            else:
                self.weapon.append(weapon)
            print("Подобрал " + str(weapon.name))
        else:
            print("Это не оружие")

    def next_weapon(self):
        if len(self.weapon) == 0:
            print("Я безоружен")
        elif len(self.weapon) == 1:
            print("У меня только одно оружие")
        else:
            indx = self.weapon.index(self.weapon_now)
            self.weapon_now = self.weapon[indx + 1]

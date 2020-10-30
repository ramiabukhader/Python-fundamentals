# properties: it is a feature of object oriented programming which enables the class to present virtual attributes

# Virtual attributes: they are normal attributes but not stored, they are computed only when requested through objects,

# simple game structer logic for game: checking if the character has taken any damage or not

class Character(object):
    def __init__(self,name,max_hp):
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp

    @property  # this is a read only definition, property makes it read only --- property makes the def only a getter but not a setter
    def hp(self):
        return self._hp

    @property
    def name(self):
        return self._name

    def take_damage(self, damage):
        self._hp -= damage
        self._hp = 0 if self._hp < 0 else self._hp

    @property
    def is_alive(self):
        return self._hp !=0

    @property
    def is_wounded(self):
        return self._hp < self._max_hp if self._hp > 0 else False

    @property
    def is_dead(self):
        return not self.is_alive


Rami = Character("Rami", 100)
print(Rami.is_alive)
print(Rami.is_wounded)

Rami.take_damage(50)
print(Rami.is_wounded)
print(Rami.hp)
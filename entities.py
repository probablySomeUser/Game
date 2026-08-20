from random import randint
import weapons

class Entity():
    def __init__(self,name: str,HP:int,AC:int,str_modifier:int,dex_modifier:int,position):
        self.name = name
        self.HP=HP
        self.AC=AC
        self.str_modifier = str_modifier
        self.dex_modifier = dex_modifier
        self.position = position

    def attack(self,target:Entity):
        target.HP -= 1
        print(self.name,'attacked',target.name)
        if type(target) == Player:
            print(target.name,'has', target.HP,'HP')
    
    def distance(self,target:Entity):
        distance = abs(self.position[0]-target.position[0])+abs(self.position[1]-target.position[1])
        return distance
    
    def kill(self,combatants):
        if self.HP <= 0 and len(combatants)>= 2 and self in combatants:
            a=combatants.index(self)
            del combatants[a]
            print(self.name,'has died')


class Player(Entity):
    def __init__(self,name:str,HP:int,AC:int,str_modifier:int,dex_modifier:int,position,weapons=[]):
        self.weapons = weapons
        super().__init__(name,HP,AC,str_modifier,dex_modifier,position)
    
    def player_attack(self,combatants):
        possible_targets = []
        for i in combatants:
            if i!= self and self.distance(i)<self.max_range():
                possible_targets.append(i)
        if possible_targets ==[]:
            print('Noone to attack')
            return
        print('Who do you want to attack?')
        counter = 1
        for i in possible_targets:
            print(counter,f') {i.name} (distance:',self.distance(i),')')
            counter += 1
        target_no = get_int(1,len(possible_targets))
        target = possible_targets[target_no-1]
        print('What weapon do you want to use')
        counter = 1
        possible_weapons = []
        for weapon in self.weapons:
            if weapon.long_range >= self.distance(target):
                possible_weapons.append(weapon)
        for weapon in possible_weapons:
            print(counter,f') {weapon.name}')
        weapon_no = get_int(1,len(possible_weapons))
        chosen_weapon = possible_weapons[weapon_no-1]
        #check if attack hits
        if self.distance(target)<= chosen_weapon.short_range:
            roll = randint(1,20)
        else:
            roll = min(randint(1,20), randint(1,20))
        print('You rolled',roll,end='.')
        if not chosen_weapon.melee or self.distance(target) >1: #Ranged attack
            if roll + self.dex_modifier >= target.AC:
                damage = chosen_weapon.damage(roll==20)+self.dex_modifier
                print(' It hits and you deal', damage,' damage')
                target.HP-= damage
            else:
                print(' It does not hit')



    def max_range(self):
        max_range = 0
        for i in self.weapons:
            if i.long_range > max_range:
                max_range = i.long_range
        return max_range

def create_player(name:str,HP:int,AC:int,str_modifier:int,dex_modifier,position,weapons=[]):
    return Player(name,HP,AC,str_modifier,dex_modifier,position,weapons)

def get_int(min_int:int,max_int:int):
    while True:
        try:
            answer = int(input())
        except:
            print('That is not a number')
            continue
        if min_int <= answer <= max_int:
            return answer
        else:
            continue

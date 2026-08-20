import entities
import weapons


spear = weapons.get_weapon('spear')
eric_withakay = entities.create_player('Eric Withakay',10,10,0,0,[0,0],[spear])
boblin = entities.create_player('Boblin',10,10,0,0,[1,1],[spear])
combatants = [eric_withakay,boblin]
eric_withakay.player_attack(combatants)
while len(combatants) > 1:
    for i in combatants:
        i.kill(combatants)
        i.player_attack(combatants)


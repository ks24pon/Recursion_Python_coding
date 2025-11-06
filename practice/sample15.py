def monsterAttackExpressionNest(monster):
    attack = 10000
    message = "'s attack is:"

    return "Cyclops" + message + str(attack*1.8) if monster == "Cyclops" else "Ogre" + message + str(attack*2.5) if monster == "Ogre" else "Zombie" + message + str(attack*1.2) if monster == "Zombie" else "Monster does not exist."


print(monsterAttackExpressionNest("Cyclops"))
print(monsterAttackExpressionNest("Ogre"))
print(monsterAttackExpressionNest("Zombie"))
print(monsterAttackExpressionNest("Ghost"))

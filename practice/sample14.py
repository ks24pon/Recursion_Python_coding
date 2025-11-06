def monsterAttack(monster):
    attack = 1000
    message = "'s attack is:"

    if monster == "Cyclops":
        attack *= 1.8
        message = "Cyclops" + message + str(attack)

    elif monster == "Ogre":
        attack *= 2.5
        message = "Ogre" + message + str(attack)

    elif monster == "Zombie":
        attack += 1.2
        message = "Zombie" + message + str(attack)

    else:
        message = "Monster does not exist."

    return message


print(monsterAttack("Ogre"))
print(monsterAttack("Ghost"))

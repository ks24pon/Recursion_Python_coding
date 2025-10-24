class PhysicsThings():
    GRAVITY = 9.8

    def getWeight(weight):
        return weight * PhysicsThings.GRAVITY

    def potentialEnergy(weight, height):
        return weight * height * PhysicsThings.GRAVITY

    def kineticEnergy(weight, sord):
        return weight * sord ** 2 / 2

print(PhysicsThings.GRAVITY)
print(PhysicsThings.getWeight(80))
print(PhysicsThings.potentialEnergy(80,4))
print(PhysicsThings.kineticEnergy(80,10))
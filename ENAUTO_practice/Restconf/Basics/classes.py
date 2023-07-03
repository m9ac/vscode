

class Circle():
    radius = 0;

    def calcCircumfrence(self):
        return 3.141 * 2 * self.radius

circleA = Circle()
circleA.radius = 15
print(circleA.calcCircumfrence())

circleB = Circle()
circleB.radius = 10
print(circleB.calcCircumfrence())

print(circleA.calcCircumfrence() - circleB.calcCircumfrence())


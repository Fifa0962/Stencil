#-----Note-----#
# Class = Blueprint for making Object
# Object = a data struture that has variable (properties) and function (methods) inside it
# a coppy of that class is Instant

# Create and change property
class Ball():
    x = 0
    y = 0
    radius = 10
    weight = 10

ball1 = Ball()
ball1.x = 20
ball1.y = 20

ball2 = Ball()
print(ball2.x)
print(ball2.y)

# Create subclass

class Circle():
    radius = 10
    color = "blue"

class Sun(Circle):
    color = "yellow"

circle1 = Circle()
print(circle1.radius)
print(circle1.color)

sun1 = Sun()
print(sun1.radius)
print(sun1.color)

class Bowlling(Ball):
    radius = 30
    weight = 9999
    quote = "it's over nine thouson!!"

bowlling1 = Bowlling
print(bowlling1.weight)
print(bowlling1.radius)
print(bowlling1.quote)

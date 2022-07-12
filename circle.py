<<<<<<< HEAD
from math import pi
=======
from email import message
from math import perm, radians
>>>>>>> dev

def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Radius must be non-negative real number only")
    if radius < 0:
<<<<<<< HEAD
        raise ValueError("Radius cant't be negative")
    return pi*radius**2
=======
        raise ValueError("Радиус не может быть отрицательный")
    return pi*radius**2


# r_line = [2, -3, 2 + 3j, True, [2], 'seven']
# message = 'Площадь окружности с радиусом {radius} --> {area}'
# 
# for r in r_line:
#     s = circle_area(r)
#     print(message.format(radius = r, area = s))
>>>>>>> dev

# octagon.py
import math

def radius_circumscribed(side_length):
    # Обчислення радіуса кола, описаного навколо правильного восьмикутника
    return side_length / (2 * math.sin(math.pi / 8))

def radius_inscribed(side_length):
    # Обчислення радіуса кола, вписаного в правильний восьмикутник
    return side_length / (2 * math.tan(math.pi / 8))

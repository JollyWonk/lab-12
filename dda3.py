import octagon

side_length = float(input("Введіть довжину сторони восьмикутника: "))

circumscribed_radius = octagon.radius_circumscribed(side_length)
inscribed_radius = octagon.radius_inscribed(side_length)

print(f"Радіус описаного кола: {circumscribed_radius}")
print(f"Радіус вписаного кола: {inscribed_radius}")

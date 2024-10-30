import random

def generate_phone_numbers(n):
    phone_numbers = []
    for _ in range(n):
        phone_number = f"(099) {random.randint(1000000, 9999999)}"
        phone_numbers.append(phone_number)
    return phone_numbers

n = int(input("Введіть кількість телефонних номерів: "))
for number in generate_phone_numbers(n):
    print(number)

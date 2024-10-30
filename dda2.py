import random

def generate_random_strings(m, n, alphabet):
    random_strings = []
    for _ in range(m):
        random_string = ''.join(random.choice(alphabet) for _ in range(n))
        random_strings.append(random_string)
    return random_strings

m = int(input("Введіть кількість рядків: "))
n = int(input("Введіть довжину рядка: "))
alphabet = input("Введіть алфавіт для рядків (напр., abcdef): ")
for string in generate_random_strings(m, n, alphabet):
    print(string)

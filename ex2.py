def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


print("=== Рівень 2. Перевірка простого числа ===")

number = int(input("Введіть ціле число: "))

if is_prime(number):
    print(f"Число {number} є простим.")
else:
    print(f"Число {number} не є простим.")
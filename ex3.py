class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Помилка: ділення на нуль неможливе"
        return a / b


print("=== Рівень 3. Клас Калькулятор ===")

calculator = Calculator()

a = 10
b = 5

print(f"Перше число: {a}")
print(f"Друге число: {b}")

print(f"Додавання: {calculator.add(a, b)}")
print(f"Віднімання: {calculator.subtract(a, b)}")
print(f"Множення: {calculator.multiply(a, b)}")
print(f"Ділення: {calculator.divide(a, b)}")
import random

def get_numbers_ticket(min, max, quantity):
    numbers = set()
    if quantity <= (max - min + 1) and min < max and min > 0 and max < 1000:
        while len(numbers) < quantity:
            number = random.randint(min, max)
            numbers.add(number)
        return sorted(numbers)
    else:
        return []
tickets = get_numbers_ticket(1, 99, 8)
print(f"Ваші лотерейні числа: {tickets}")

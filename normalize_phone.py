import re

def normalize_phone(phone_number):
    
    sanitized_numbers = []
    for number in phone_number:
        digits = re.sub(r"\D", "", number)
        digits = re.sub(r"^(380|38|0)", "", digits)
        if len(digits) == 9:
            digits = "+380" + digits
            sanitized_numbers.append(digits)
        else:
            sanitized_numbers.append("Invalid number: " + digits.strip())
    return sanitized_numbers

phone_number = [
    "067\\t123 4567",
    "(95) 234-5678\\n",
    "+380 44 123 4567",
    "83050 123 32 34",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

normalized_numbers = normalize_phone(phone_number)
print("Нормалізовані номери телефонів для SMS-розсилки:", normalized_numbers)
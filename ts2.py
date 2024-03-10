import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'[-+]?\b\d+\.\d+\b|\b\d+\b'  
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    total = sum(func(text))
    return total
 

text = "Дохід від продажу: 500.55 грн; додаткові прибутки: +100.10 і -50.25 грн."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний прибуток: {total_income} грн")



weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))
if height > 3:
    height = height/100

bmi = weight / (height ** 2)
print(bmi)
print(f'''
    --- Отчет о состоянии здоровья ---
    Рост:\t{height} кг
    Вес:\t{weight} см
    Индекс массы тела:\t{bmi:.2f}
''')
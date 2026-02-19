nutrient_medium_name = input("Название питательной среды: ")
agar_percentage_concentration = input("Концентрация агара (%): ")
sterilization_temperature = input("Температура стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as card:
    card.write(f'{nutrient_medium_name}\nКонцентрация агара (%)\t{agar_percentage_concentration}\nТемпература стерилизации\t{sterilization_temperature}')
    
    print(f"Файл 'recipe.txt' успешно сформирован!")
    
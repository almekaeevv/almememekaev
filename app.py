def multiplication_table():
    table = ""
    for i in range(1, 11):
        row = ""
        for j in range(1, 11):
            row += str(i * j).rjust(4)  # Правильное выравнивание чисел в строках
        table += row + "\n"
    
    # Для отображения таблицы в алерте в браузере, можно будет использовать:
    # alert(table) через JavaScript, но в Python просто выводим таблицу в консоль
    print(table)

multiplication_table()

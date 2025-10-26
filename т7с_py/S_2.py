import csv

def add_expense():
    item = input("На что потратили: ")
    amount = input("Сколько: ")

    with open('expenses.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([item, amount])

    print("Запись добавлена!")

def show_expenses():
    try:
        with open('expenses.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            print("\n=== РАСХОДЫ ===")
            for row in reader:
                print(f"{row[0]} - {row[1]} руб.")
    except:
        print("Расходов нет")

while True:
    print("\n1. Добавить расход")
    print("2. Показать расходы")
    print("3. Выход")

    choice = input("Выберите: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        break
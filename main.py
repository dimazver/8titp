import random
import string

class TextHandler:
    def __init__(self):
        self.text = ""
        self.ans = []
        self.writed = False
        self.chandeg = False

    def get_text(self):
        self.writed = True
        print("\nВведите текст")
        self.text = str(input())

    def gen_text(self):
        self.writed = True
        print("\nВведите длину текста")
        len_txt = int(input())
        all_symbols = string.ascii_uppercase + " "
        self.text = ''.join(random.choice(all_symbols) for _ in range(len_txt))

    def palindrome(self):
        if self.writed:
            self.chandeg = True
            list_of_words = self.text.split()
            self.ans = [word for word in list_of_words if word == word[::-1]]
        else:
            print("Сначала введите текст")

    def result(self):
        if self.chandeg:
            if not self.ans:
                print("Палиндромов не обнаружено")
            else:
                print(self.ans)
        else:
            print("Сначала проверьте текст на палиндромы")

    def pretty(self):
        pass

def print_menu():
    """Выводит меню с доступными заданиями."""
    print("\nВыберете пункт меню")
    print("1. Ввод исходных данных вручную")
    print("2. Ввод исходных данных сгенерированных случайным образом")
    print("3. Выполнение алгоритма по заданию")
    print("4. Вывод результата")
    print("5. Завершение работы программы")

def main():
    """Основная функция программы, которая управляет выбором задания пользователем."""
    text_handler = TextHandler()

    while True:
        print_menu()  # Выводим меню
        choice = int(input("Выберите пункт меню: "))  # Запрашиваем выбор пользователя

        if choice == 1:
            text_handler.get_text()
            text_handler.chandeg = False
        elif choice == 2:
            text_handler.gen_text()
            text_handler.chandeg = False
        elif choice == 3:
            text_handler.palindrome()
        elif choice == 4:
            text_handler.result()
        elif choice == 5:
            print("Завершение работы программы.")  # Сообщаем о завершении
            break  # Выходим из цикла
        else:
            print("Неверный выбор.")  # Обработка неверного выбора

if __name__ == "__main__":
    main()  # Запуск основной функции при выполнении скрипта

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
        self.text = input("\nВведите текст: ")

    def gen_text(self):
        self.writed = True
        len_txt = int(input("\nВведите длину текста: "))
        all_symbols = string.ascii_uppercase + " "
        self.text = ''.join(random.choice(all_symbols) for _ in range(len_txt))

    def is_palindrome(self, word):
        return word == word[::-1]

    def find_palindromes(self):
        if self.writed:
            self.chandeg = True
            list_of_words = self.text.split()
            self.ans = [word for word in list_of_words if self.is_palindrome(word)]
        else:
            print("Сначала введите текст")

    def display_result(self):
        if self.chandeg:
            if not self.ans:
                print("Палиндромов не обнаружено")
            else:
                print(" ".join(self.ans))
        else:
            print("Сначала проверьте текст на палиндромы")

def print_menu():
    """Выводит меню с доступными заданиями."""
    print("\nВыберете пункт меню:")
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

        (choice == 1 and text_handler.get_text()) or \
        (choice == 2 and text_handler.gen_text()) or \
        (choice == 3 and text_handler.find_palindromes()) or \
        (choice == 4 and text_handler.display_result()) or \
        (choice == 5 and (print("Завершение работы программы."), exit())) or \
        print("Неверный выбор.")  # Обработка неверного выбора

if __name__ == "__main__":
    main()  # Запуск основной функции при выполнении скрипта

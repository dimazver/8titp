import random
import string

class TextHandler:
    def __init__(self):
        pass

    def get_text(self):
        pass

    def gen_text(self):
        pass

    def palindrome(self):
        pass

    def result(self):
        pass



def main():

    text_handler = TextHandler()

    while True:

        choice = int(input("Выберите пункт меню: "))

        if choice == 1:
            text_handler.get_text()
        elif choice == 2:
            text_handler.gen_text()
        elif choice == 3:
            text_handler.palindrome()
        elif choice == 4:
            text_handler.result()
        elif choice == 5:
            print("Завершение работы программы.")
            break  # Выходим из цикла
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()

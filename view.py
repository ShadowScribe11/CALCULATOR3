from loguru import logger


def user_menu():
    logger.info("Пользоватьльское меню вызвано")
    print("Добрый день, я бот-шифтратор")
    print("Я могу зашифровать и расшифровать любое послание!")

    print("1. Зашифровать строку")
    print("2. Расшифровать строку")
    print("3. Выход")
    answer = int(input("Введите свой вариант: "))
    if answer == 1:
        line = user_input("Введите строки для шифрования: ")
        return [line, 1]
    elif answer == 2:
        line = user_input("Введите строки для расшифровки: ")
        return [line, 2]
    elif answer == 3:
        return ["", 3]
    else:
        print("Введите один из трех вариантов!")


def user_input(settings):
    line = input(settings)
    return line


def answer_with_result(line):
    print(line)
from datetime import datetime

from Controller import *


def start():
    command = input('\nДоступные команды:\n'
                    '1. ADD - создать заметку\n'
                    '2. REMOVE - удалить заметку\n'
                    '3. CLEAN - очистить все заметки\n'
                    '4. UPDATE - обновить заметку\n'
                    '5. READ - прочитать заметку\n'
                    '6. LIST - вывести весь список заметок\n'
                    '7. EXIT - выход\n'
                    'Введите команду: ')

    if command.lower().replace(' ', '') == 'add':
        name = input_text("Заголовок заметки: ")
        text = input_text("Тело заметки: ")
        controller.add(Note(name, text))
        is_end()
    elif command.lower().replace(' ', '') == 'remove':
        remove_note = input_text("Заголовок заметки, которую хотите стереть: ")
        controller.remove(remove_note)
        is_end()
    elif command.lower().replace(' ', '') == 'clean':
        controller.clean()
        is_end()
    elif command.lower().replace(' ', '') == 'update':
        name = input_text("Заголовок заметки, которую хотите обновить: ")
        controller.update(name)
        is_end()
    elif command.lower().replace(' ', '') == 'read':
        name = input_text("Заголовок заметки, которую хотите прочитать: ")
        controller.read(name)
        is_end()
    elif command.lower().replace(' ', '') == 'list':
        controller.all_notes()
        is_end()
    elif command.lower().replace(' ', '') == 'exit':
        return
    else:
        print('Нет такой команды')
        start()


def is_end():
    word = input('Продолжить... (y/n): ')
    if word.lower().replace(' ', '') == 'y':
        start()


def input_text(message):
    new_text = input(message)
    while len(new_text) < 1:
        print('Минимальная длина строки 1')
        new_text = input_text(message)
    return new_text


if __name__ == '__main__':
    controller = Controller()
    print('Привет, это твои заметки, ниже ознакомься с инструкцией')
    start()
    controller.save()

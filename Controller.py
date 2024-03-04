from Note import *
from JSON_repository import *


class Controller:
    def __init__(self):
        self.__dict = pull_json()

    def add(self, new_note):
        for item in self.__dict['notes']:
            if item['name'] == new_note.name:
                print('Заметка с таким именем уже есть!')
                return

        self.__dict['notes'].append({'id': self.__dict['amount'] + 1,
                                     'name': new_note.name,
                                     'text': new_note.text,
                                     'last_interaction_date': new_note.last_interaction_date})
        self.__dict['amount'] += 1
        print('Заметка добавлена!')

    def remove(self, name):
        for i in range(len(self.__dict['notes'])):
            if self.__dict['notes'][i]['name'] == name:
                confirm = input(f'Вы действительно хотите удалить заметку '
                                f'"{self.__dict["notes"][i]["name"]}": '
                                f'"{self.__dict["notes"][i]["text"]}" от '
                                f'{self.__dict["notes"][i]["last_interaction_date"]}\n'
                                f'Подтвердить... (y/n): ')
                if confirm.lower().replace(' ', '') == "y":
                    self.__dict['notes'].pop(i)
                    self.__dict['amount'] -= 1
                    for j in range(i, len(self.__dict['notes'])):
                        self.__dict['notes'][j]['id'] -= 1
                    print('Заметка удалена!')
                    return
        print('Заметка не найдена...')

    def all_notes(self):
        is_reverse = input('Введите:\n'
                           '1 - сначала старые\n'
                           '2 - сначала новые\n'
                           'Ваш выбор: ')
        if is_reverse == '1':
            for i in range(len(self.__dict['notes'])):
                print(f'{i + 1}. Заголовок: {self.__dict["notes"][i]["name"]}\n'
                      f'Тело заметки: {self.__dict["notes"][i]["text"]}\n'
                      f'Последнее взаимодействие: {self.__dict["notes"][i]["last_interaction_date"]}\n')
        elif is_reverse == '2':
            self.__dict['notes'].reverse()
            for i in range(len(self.__dict['notes'])):
                print(f'{i + 1}. Заголовок: {self.__dict["notes"][i]["name"]}\n'
                      f'Тело заметки: {self.__dict["notes"][i]["text"]}\n'
                      f'Последнее взаимодействие: {self.__dict["notes"][i]["last_interaction_date"]}\n')
            self.__dict['notes'].reverse()
        else:
            self.all_notes()

    def clean(self):
        confirm = input('Вы действительно хотите очистить ВСЕ заметки (y/n): ')
        if confirm == 'y':
            print('Очистка...')
            self.__dict['notes'].clear()
            self.__dict['amount'] = 0
            print('Очистка прошла успешно')
        else:
            print('Ура, заметки не удалены!')

    def update(self, name):
        for i in range(len(self.__dict['notes'])):
            if self.__dict['notes'][i]['name'] == name:
                confirm = input('Введите:\n'
                                '1 - изменить заголовок заметки\n'
                                '2 - изменить содержимое заметки\n'
                                'Ваш выбор: ')
                if confirm == '1':
                    self.__dict['notes'][i]['name'] = input('Введите новый заголовок заметки: ')
                    print('Заметка обновлена')
                elif confirm == '2':
                    self.__dict['notes'][i]['text'] = input('Введите новый текст заметки: ')
                    print('Заметка обновлена')
                else:
                    self.update(name)
                return
        print('Заметка не найдена...')

    def read(self, name):
        for i in range(len(self.__dict['notes'])):
            if self.__dict['notes'][i]['name'] == name:
                print(f'Заголовок: {self.__dict["notes"][i]["name"]}\n'
                      f'Тело заметки: {self.__dict["notes"][i]["text"]}\n'
                      f'Последнее взаимодействие: {self.__dict["notes"][i]["last_interaction_date"]}\n')
                return
        print('Заметка не найдена...')

    def save(self):
        push_json(self.__dict)

    @property
    def dict(self):
        return self.__dict

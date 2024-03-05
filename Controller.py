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
                else:
                    return
        print('Заметка не найдена...')

    def all_notes(self):
        is_reverse = input('Введите:\n'
                           '1 - сначала старые по дате создания\n'
                           '2 - сначала новые по дате создания\n'
                           '3 - выборка по дате от и до\n'
                           '4 - назад\n'
                           'Ваш выбор: ')
        if is_reverse == '1':
            for note in self.__dict['notes']:
                self.print_note(note)
        elif is_reverse == '2':
            self.__dict['notes'].reverse()
            for note in self.__dict['notes']:
                self.print_note(note)
            self.__dict['notes'].reverse()
        elif is_reverse == '3':
            print('Введите дату и время в формате <<1.1.2001 13:00>>')
            start_selection = input('От: ')
            end_selection = input('До: ')
            try:
                start_selection = datetime.strptime(start_selection, '%d.%m.%Y %H:%M')
                end_selection = datetime.strptime(end_selection, '%d.%m.%Y %H:%M')
                count = 0
                for note in self.__dict['notes']:
                    if (start_selection
                            < datetime.strptime(note['last_interaction_date'], '%d.%m.%Y %H:%M')
                            < end_selection):
                        count += 1
                        self.print_note(note)
                if count == 0:
                    print('Заметки не найдены')
            except:
                print('Неправильно введены параметры даты и времени')
                self.all_notes()
        elif is_reverse == '4':
            return
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
                                '3 - назад\n'
                                'Ваш выбор: ')
                if confirm == '1':
                    self.__dict['notes'][i]['name'] = input('Введите новый заголовок заметки: ')
                    self.__dict['notes'][i]['last_interaction_date'] = datetime.now().strftime('%d.%m.%Y %H:%M')
                    print('Заметка обновлена')
                elif confirm == '2':
                    self.__dict['notes'][i]['text'] = input('Введите новый текст заметки: ')
                    self.__dict['notes'][i]['last_interaction_date'] = datetime.now().strftime('%d.%m.%Y %H:%M')
                    print('Заметка обновлена')
                elif confirm == '3':
                    return
                else:
                    print('Команда не найдена!')
                    self.update(name)
                return
        print('Заметка не найдена...')

    def read(self, name):
        for note in self.__dict['notes']:
            if note['name'] == name:
                self.print_note(note)
                return
        print('Заметка не найдена...')

    def save(self):
        push_json(self.__dict)

    def print_note(self, note):
        print(f'ID заметки: {note["id"]}\n'
              f'Заголовок: {note["name"]}\n'
              f'Тело заметки: {note["text"]}\n'
              f'Последнее взаимодействие: {note["last_interaction_date"]}\n')

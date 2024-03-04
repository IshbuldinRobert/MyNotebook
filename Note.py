from datetime import datetime


class Note:
    def __init__(self, name, text):
        self.__name = name
        self.__text = text
        self.__last_interaction_date = datetime.now().strftime('%d.%m.%Y %H:%M')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text):
        self.__text = new_text

    @property
    def last_interaction_date(self):
        return self.__last_interaction_date

    @last_interaction_date.setter
    def last_interaction_date(self, new_date):
        self.__last_interaction_date = new_date

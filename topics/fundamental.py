'''class BaseTheme:
    description: str
    key_words: str
    instances: list

    def __init__(self):
        self.__class__.instances.append(self.__class__.__name__)


class InstanceTheme:
    name: str
    author: str'''


###############################################
###############################################

class Fundamental:

    def __init__(self):
        super().__init__()


class Инструменты_Методы_Связи_С_Внешним(Fundamental):

    def __init__(self):
        super().__init__()


class Исследование_Роли_Понятия_Феномена(Fundamental):

    def __init__(self):
        super().__init__()


class Поиск_новых_оснований(Fundamental):

    def __init__(self):
        super().__init__()


class Отношения_Динамичного_контекста_и_Статичной_Архитектуры(Инструменты_Методы_Связи_С_Внешним):

    def __init__(self):
        super().__init__()


class Коммуникация_с_архитектурой(Поиск_новых_оснований, Инструменты_Методы_Связи_С_Внешним):

    def __init__(self):
        super().__init__()


class Субъект_Объект_Пространство(Исследование_Роли_Понятия_Феномена):

    def __init__(self):
        super().__init__()


class Критика_Понятия_Предложение_Инструмента(Поиск_новых_оснований, Исследование_Роли_Понятия_Феномена):

    def __init__(self):
        super().__init__()


class Этическое_Рефлексия_Восприятие(Исследование_Роли_Понятия_Феномена):

    def __init__(self):
        super().__init__()

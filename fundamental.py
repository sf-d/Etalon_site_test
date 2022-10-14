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


class Инструменты_Методы_Для_Описания(Fundamental):

    def __init__(self):
        super().__init__()


class Исследование_Роли_Понятия_Феномена(Fundamental):

    def __init__(self):
        super().__init__()


class Поиск_новых_оснований(Fundamental):

    def __init__(self):
        super().__init__()


class Отношения_внешнего_и_внутреннего(Инструменты_Методы_Для_Описания, Исследование_Роли_Понятия_Феномена):

    def __init__(self):
        super().__init__()


class Рефлексия(Исследование_Роли_Понятия_Феномена, Поиск_новых_оснований):

    def __init__(self):
        super().__init__()
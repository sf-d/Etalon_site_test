class BaseTheme:
    description: str
    key_words: str
    instances: list

    def __init__(self):
        self.__class__.instances.append(self.__class__.__name__)


class InstanceTheme:
    name: str
    author: str



###############################################
###############################################

class Fundamentals(BaseTheme):

    def __init__(self):
        super().__init__()


class DescriptionMethodsInstruments(Fundamentals):
    description = 'принцип рассмотрения / изучения архитектуры, инструментарий для описания'

    def __init__(self):
        super().__init__()


###############################################
###############################################
class Abstract(BaseTheme):

    def __init__(self):
        super().__init__()


class MediaLanguage(Abstract):

    def __init__(self):
        super().__init__()


class SocialCulture(Abstract):

    def __init__(self):
        super().__init__()


###############################################
###############################################


class InnerOuterBound(DescriptionMethodsInstruments):
    description = 'принцип рассмотрения / изучения архитектуры, инструментарий для описания'

    def __init__(self):
        super().__init__()


###############################################
###############################################

class ArchAsDescrLang(InnerOuterBound, MediaLanguage, SocialCulture):
    name = 'Архитектура как язык описания: архитектурная этнография, визуальная антропология, производство знания'
    author = 'Влад Капустин'


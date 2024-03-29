class ServerError(Exception):
    '''
    Класс - исключение, для обработки ошибок сервера.
    При генерации требует строку с описанием ошибки,
    полученную с сервера.
    '''

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


# Ошибка - отсутствует обязательное поле в принятом словаре.
class RequiredFieldMissingError(Exception):
    def __init__(self, missing_field):
        self.missing_field = missing_field

    def __str__(self):
        return f'В принятом словаре отсутствует обязательное поле {self.missing_field}.'

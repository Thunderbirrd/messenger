import sys
sys.path.append('../')
import logs.client_log_config
import logs.server_log_config
import logging, socket

# метод определения модуля, источника запуска.
if sys.argv[0].find('client') == -1:
    # если не клиент то сервер!
    logger = logging.getLogger('server')
else:
    # раз не сервер, то клиент
    logger = logging.getLogger('client')


def log(logging_func):
    def log_saver(*args, **kwargs):
        logger.debug(
            f'Была вызвана функция {logging_func.__name__} c параметрами {args} , {kwargs}.'
            f' Вызов из модуля {logging_func.__module__}')
        res = logging_func(*args, **kwargs)
        return res
    return log_saver


# Функция провекрки авторизованности пользователя
def login_required(func):
    def checker(*args, **kwargs):
        # Если первый аргумент - экземпляр MessageProcessor
        # А сокет в остальных аргументах
        # Импортить необходимо тут, иначе ошибка рекурсивного импорта.
        from server.core import MessageProcessor
        from basic_things.main_variables import ACTION, PRESENCE
        if isinstance(args[0], MessageProcessor):
            found = False
            for arg in args:
                if isinstance(arg, socket.socket):
                    # Проверяем, что данный сокет есть в списке names класса MessageProcessor
                    for client in args[0].names:
                        if args[0].names[client] == arg:
                            found = True

            # Теперь надо проверить, что передаваемые аргументы не presence сообщение
            for arg in args:
                if isinstance(arg, dict):
                    if ACTION in arg and arg[ACTION] == PRESENCE:
                        found = True
            # Если не не авторизован и не сообщение начала авторизации, то вызываем исключение.
            if not found:
                raise TypeError

        return func(*args, **kwargs)

    return checker

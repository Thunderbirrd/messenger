import sys
import logs.client_log_config
import logs.server_log_config
import logging

# метод определения модуля, источника запуска.
if sys.argv[0].find('client') == -1:
    # если не клиент то сервер!
    logger = logging.getLogger('server')
else:
    # ну, раз не сервер, то клиент
    logger = logging.getLogger('client')


def log(logging_func):
    def log_saver(*args, **kwargs):
        logger.debug(
            f'Была вызвана функция {logging_func.__name__} c параметрами {args} , {kwargs}.'
            f' Вызов из модуля {logging_func.__module__}')
        res = logging_func(*args, **kwargs)
        return res
    return log_saver

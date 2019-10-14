import sys
import logging
import datetime
import logs.server_log_config
import logs.client_log_config

# определяем, откуда был вызван декоратор(сервер или клиент)
if sys.argv[0].find('client') == -1:
    logger = logging.getLogger('server')
else:
    logger = logging.getLogger('client')


def log(logging_func):
    def log_saver(*args, **kwargs):
        logger.debug(f"Была вызвана функция {logging_func.__name__} c параметрами {args} , {kwargs}. Вызов из модуля"
                     f" {logging_func.__module__}")
        if logging_func.__module__ == '__main__':
            logger.debug(f"Функция {logging_func.__name__} вызвана из функции 'main' в {datetime.datetime.now()}")
        result = logging_func(*args, **kwargs)
        return result
    return log_saver

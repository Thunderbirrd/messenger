import sys
sys.path.append('../')
import logging.handlers
import os
from basic_things.main_variables import LOGGING_LEVEL

server_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# файл, куда будут записываться логи
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'server.log')

stream = logging.StreamHandler(sys.stderr)
stream.setFormatter(server_formatter)
stream.setLevel(logging.ERROR)
log_file = logging.handlers.TimedRotatingFileHandler(path, encoding='utf8', interval=1, when='D')
log_file.setFormatter(server_formatter)

logger = logging.getLogger('server')
logger.addHandler(stream)
logger.addHandler(log_file)
logger.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    logger.critical('Test critical event')
    logger.error('Test error event')
    logger.debug('Test debug event')
    logger.info('Test info event')

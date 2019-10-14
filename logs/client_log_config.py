import sys
import os
sys.path.append('../')
import logging
from basic_things.main_variables import LOGGING_LEVEL

client_formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'client.log')

stream = logging.StreamHandler(sys.stderr)
stream.setFormatter(client_formatter)
stream.setLevel(logging.ERROR)
log_file = logging.FileHandler(path, encoding='utf8')
log_file.setFormatter(client_formatter)

logger = logging.getLogger('client')
logger.addHandler(stream)
logger.addHandler(log_file)
logger.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    logger.critical('Test critical event')
    logger.error('Test error event')
    logger.debug('Test debug event')
    logger.info('Test info event')

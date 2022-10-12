from cgitb import handler
from distutils.log import INFO
import logging
import time
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2kb, and keep nacl logs app.log.1, app.log 2, etc.

'''handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)'''

handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello, World!')
    time.sleep(5)
    

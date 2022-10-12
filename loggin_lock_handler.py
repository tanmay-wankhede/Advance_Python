import logging
import logging.config

logging.config.fileConfig('logging.conf')
'''logger = logging.getLogger(__name__)'''
'''# create handler

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s ')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logging.addHandler(stream_h)
logging.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is a error')'''


logger = logging.getLogger('simpleExample')
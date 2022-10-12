from cmath import log
import logging

'''logger = logging,logging.getLogger(__name__)
   logger.info('Hello from helper")
import (whatever file name)'''



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    datefmt='%m/%d/%Y %H:%M:%S:' )

'''import loggin_helper
logger.info('hello from helper')'''

logging.debug("This is a debug message")
logging.info('This is an info message')
logging.warning('This is a warnging message')
logging.error('This is an error message')
logging.critical('This is a critical message')

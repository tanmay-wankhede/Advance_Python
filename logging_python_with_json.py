from cgitb import handler
from distutils.log import INFO
import logging
import time
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler 
from pythonjsonlogger import jsonlogger

    logger = logging.getLogger()

    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
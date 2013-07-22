import logging
logger = logging.getLogger('uvclight.uvc.tb_layout')

def log(message, summary='', severity=logging.DEBUG):
    logger.log(severity, '%s %s', summary, message)

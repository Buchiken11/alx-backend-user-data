import logging
import mylib

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
    logger.info("Started")
    logger.debug('This message should go to the log file')
    logger.info('So should this')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
    mylib.do_something()
    logger.info('Finished')

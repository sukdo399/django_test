#!/usr/bin/env python
import os
import sys
import logging.handlers


if __name__ == "__main__":
    # logger setting
    formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

    logger = logging.getLogger('logger')

    fileMaxByte = 1024 * 1024 * 20  # 20MB
    fileHandler = logging.handlers.RotatingFileHandler('log.log', maxBytes=fileMaxByte, backupCount=1, encoding='utf-8')
    # fileHandler = logging.FileHandler('./log.log')
    streamHandler = logging.StreamHandler()

    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    logger.setLevel(logging.DEBUG)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_server.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

#!/bin/python3
# -*- coding: utf-8 -*-

import logging

# Конфигурация логера

class MegaHandler(logging.Handler):
    def __init__(self, filename):
        logging.Handler.__init__(self)
        self.filename = filename

    def emit(self, record):
        message = self.format(record)
        with open(self.filename, 'a') as file:
            file.write(message + '\n')


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format_stream': {
            'format': '{asctime} - {levelname} - \t(module:{module} line:{lineno}) - {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'std_format_file': {
            'format': '{asctime} - {levelname} - {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'formatter': 'std_format_stream'
        },
        'file': {
            '()': MegaHandler,
            'level': 'INFO',
            'filename': 'nms.log',
            'formatter': 'std_format_file'
        }
    },
    'loggers': {
        'nms_logger': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
            'propagate': True
        }
    },

    # 'filters': {},
    # 'root': {}   # '': {}
    # 'incremental': True
}

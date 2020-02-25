import logging
from logging.handlers import RotatingFileHandler, QueueListener
import os
from logging.config import dictConfig
import queue


class Logging:
    PATH_LOGS = "/var/log/bot/"
    FULL_FORMAT = "[%(asctime)s " \
                  "%(levelname)s " \
                  "%(name)s] " \
                  "[%(thread)d " \
                  "%(threadName)s %(process)d] " \
                  "[%(pathname)s " \
                  "%(funcName)s " \
                  "%(func)s] " \
                  "[%(exc_info) " \
                  "%(lineno)d] " \
                  "%(message)s"
    SHORT_FORMAT = "%(asctime)s " \
                   "%(levelname)s " \
                   "%(name)s " \
                   "%(pathname)s " \
                   "%(threadName)s " \
                   "%(message)s"
    DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

    def init(self, name, logs_queue: queue.Queue=None):
        if not os.path.exists(self.PATH_LOGS):
            os.mkdir(self.PATH_LOGS)
        self.short_formatter = logging.Formatter(self.SHORT_FORMAT, datefmt=self.DATE_FORMAT)
        self.long_formatter = logging.Formatter(self.FULL_FORMAT, datefmt=self.DATE_FORMAT)
        self.logger = logging.getLogger(name)
        self.file_handler = self.file_handler()
        self.stream_handler = self.stream_handler()
        self.logger.addHandler([handl for handl in [self.file_handler, self.stream_handler]])
        self.logger.setLevel(logging.DEBUG)

    def repr(self):
        return self.logger

    def file_handler(self):
        handler = RotatingFileHandler(f"{self.PATH_LOGS}/logs_.log", maxBytes=2000, backupCount=100)
        handler.setFormatter(self.long_formatter)
        return handler

    def stream_handler(self):
        handler = logging.StreamHandler()
        handler.setFormatter(self.short_formatter)
        return handler


log = Logging(__name__)

log.info("Pizdec suka cho delat")


class LogsQueue:
    def init(self, logs):
        self.WAIT_TIMEOUT = 1
        self.logs_queue = queue.Queue()
        self.log = logs

    def put_log(self):
        self.logs_queue.put(self.log)

    def pop_log(self):
        log = self.logs_queue.get(timeout=self.WAIT_TIMEOUT)
        self.logs_queue.task_done()
        return log

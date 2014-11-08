__author__ = 'trs'

import logging
from cryptoknocker_db import get_port_serviceName

class PortLog():
    def __init__(self):
        self.LOG_FILE_PATH = "../logs/port.log"

    def log_port_status(self, port, status, username, client_ip):
        logging.basicConfig(format='%(asctime)s %(message)s' ,filename=self.LOG_FILE_PATH, level=logging.INFO)
        serviceName = get_port_serviceName(port)
        logging.info("%s %s %s %s %s"%(port, serviceName, status, username, client_ip))

    def log_port_error(self, message):
        logging.basicConfig(format='%(asctime)s %(message)s' ,filename=self.LOG_FILE_PATH, level=logging.WARNING)
        logging.WARNING(message)


class ServerLog():
    def __init__(self):
        self.LOG_FILE_PATH = "../logs/server.log"

    def log_login(self, username):
        logging.basicConfig(format='%(asctime)s %(message)s' ,filename=self.LOG_FILE_PATH, level=logging.INFO)
        logging.info("%s login")

    def log_logout(self, username):
        logging.basicConfig(format='%(asctime)s %(message)s' ,filename=self.LOG_FILE_PATH, level=logging.INFO)
        logging.info("%s logout")
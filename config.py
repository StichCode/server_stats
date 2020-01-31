import os


class Config(object):
    TOKEN = os.environ.get("TOKEN")
    USERNAME_SOCKS = os.environ.get("USERNAME_SOCKS")
    PASSWORD_SOCKS = os.environ.get("PASSWORD_SOCKS")
    ADDRESS_SOCKS = os.environ.get("ADDRESS_SOCKS")
    PORT_SOCKS = os.environ.get("PORT_SOCKS")

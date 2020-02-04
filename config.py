import os


class Config(object):
    TOKEN = os.environ.setdefault("TOKEN", None)
    USERNAME_SOCKS = os.environ.setdefault("USERNAME_SOCKS", None)
    PASSWORD_SOCKS = os.environ.setdefault("PASSWORD_SOCKS", None)
    ADDRESS_SOCKS = os.environ.setdefault("ADDRESS_SOCKS", None)
    PORT_SOCKS = os.environ.setdefault("PORT_SOCKS", None)

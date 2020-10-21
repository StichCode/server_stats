from datetime import datetime
from typing import NamedTuple

from loguru import logger


class Config(NamedTuple):
    token: str
    admin: str

    def __str__(self):

        fields = {
            "token": self.token,
            "admin": self.admin
        }

        body = '\n'.join(
            ("\t{0:10}: {1}".format(descr, val) for descr, val in fields.items())
        )
        return "\n{0}\tParameters for >this< ({1}) run: \n{2}\n{0}".format('= '*6, datetime.now(), body)


#os.environ.setdefault("TOKEN", "935219929:AAGZkRiF3uGRcYewimNIcd8bSNm1pD5E72k"),
config = Config(
    token="947929664:AAG64VfAaYKJ3mOcJuwGLCZX4irWUc21Nm4",
    admin="295290188"
)

logger.info(config)
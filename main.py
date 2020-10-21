import threading

from loguru import logger

from src.functions.bot import start_bot
from src.functions.health import health_tick_bot


def main():
    logger.info("Start bot")
    [threading.Thread(target=thr).start() for thr in [start_bot, health_tick_bot]]


if __name__ == '__main__':
    main()
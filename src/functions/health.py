from time import sleep

from loguru import logger


def health_tick_bot(tick: int = 20):
    while True:
        logger.info("Bot is available")
        sleep(tick)
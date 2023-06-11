import argparse
import logging
import os
import sys

from argparse import ArgumentParser

from external.gcp import GCPFacade
from external.tg import TelegramFacade
from bot import Speech2TextBot


logger = logging.getLogger('telegram-speech2text-bot')
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def get_args():
    parser = ArgumentParser()
    parser.add_argument("--webhook", default=True, action=argparse.BooleanOptionalAction)
    parser.add_argument("--telegram-token", default=os.environ.get('UTRUST_TELEGRAM_TOKEN', None))
    parser.add_argument("--secret-token", default=os.environ.get('UTRUST_SECRET_TOKEN', None), type=str)
    parser.add_argument("--url", default=os.environ.get('UTRUST_URL', None), type=str)
    parser.add_argument("--port", default=int(os.environ.get("UTRUST_PORT", 8080)), type=int)
    parser.add_argument("--language", default=os.environ.get("UTRUST_LANGUAGE", "en-US"), type=str)

    parser.add_argument("--speech-to-text-workspace", default=os.environ.get('UTRUST_SPEECH_TO_TEXT_WORKSPACE', None))
    return parser.parse_args()


def main(webhook: bool,
         telegram_token: str,
         speech_to_text_workspace: str,
         port: int,
         secret_token: str,
         language: str,
         url: str):
    gcp = GCPFacade(speech_to_text_workspace, language)
    tg = TelegramFacade(telegram_token)

    bot = Speech2TextBot(gcp, tg, )
    if webhook:
        bot.run_webhook(port, secret_token, url)
    else:
        bot.run_polling()


if __name__ == '__main__':
    args = get_args()
    logger.info(args)
    main(**vars(args))

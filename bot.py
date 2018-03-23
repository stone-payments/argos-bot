"""Bot starts a telegram bot."""
import os
from telegram.ext import Updater, CommandHandler
from git import handlers
import logging

LOG_FORMAT = ("%(levelname) -10s %(asctime)s %(name) "
              "-30s %(funcName) -35s %(lineno) -5d: %(message)s")

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

updater = Updater(os.getenv('TELEGRAM_BOT_TOKEN', ''))

updater.dispatcher.add_handler(CommandHandler('pull_requests', handlers.pull_requests))

updater.start_polling()
updater.idle()

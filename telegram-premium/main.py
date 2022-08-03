import logging
import argparse
import telegram.ext as tg_ext
from bot import handelrs

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def parse_args():
    """Парсер для аргумента --token"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", type=str, required=True)
    return parser.parse_args()


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    args = parse_args()
    application = tg_ext.Application.builder().token(args.token).build()

    # on different commands - answer in Telegram
    handelrs.setup_handlers(application)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()

from calendar import c
import imp
import telegram as tg
import telegram.ext as tg_ext
import abc
import typing as tp
from bot import messages


class BaseHandler(abc.ABC):
    def __init__(self) -> None:
        self.user: tp.Optional[tg.User] = None

    async def __call__(
        self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE
    ) -> None:
        self.user = update.effective_user
        self.messages = messages.get_messages(self.user)
        await self.handle(update, context)

    @abc.abstractclassmethod
    async def handle(
        self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE
    ) -> None:
        raise NotImplemented


class StartHandler(BaseHandler):
    async def handle(
        self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE
    ) -> None:
        self.messages.start()
        await update.message.reply_text(self.messages.start())


class HelpHandler(BaseHandler):
    async def handle(
        self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE
    ) -> None:
        await update.message.reply_text(self.messages.help())


class EchoHandler(BaseHandler):
    async def handle(
        self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE
    ) -> None:
        await update.message.reply_text(
            self.messages.echo(update.message.text)
        )


def setup_handlers(application: tg_ext.Application):
    # on different commands - answer in Telegram
    application.add_handler(tg_ext.CommandHandler("start", StartHandler()))
    application.add_handler(tg_ext.CommandHandler("help", HelpHandler()))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(
        tg_ext.MessageHandler(
            tg_ext.filters.TEXT & ~tg_ext.filters.COMMAND, EchoHandler()
        )
    )

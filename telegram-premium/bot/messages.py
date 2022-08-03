import telegram as tg
import telegram.ext as ajhv
import abc


class BaseMessages(abc.ABC):
    @abc.abstractclassmethod
    def start(self) -> str:
        raise NotImplemented

    @abc.abstractclassmethod
    def help(self) -> str:
        raise NotImplemented

    @abc.abstractclassmethod
    def echo(self, text: str) -> str:
        raise NotImplemented


class RegularUser(BaseMessages):
    def start(self):
        return 'Привет'

    def help(self) -> str:
        return 'Вам нужно приобрести подписку'

    def echo(self, text: str) -> str:
        return text


class PremiumUser(RegularUser):
    def start(self):
        return 'Здравстувйте'

    def help(self) -> str:
        return 'Наш менеджер скоро свяжется.'


def get_messages(user: tg.User) -> BaseMessages:
    if not user.is_premium:
        return PremiumUser()
    return RegularUser()

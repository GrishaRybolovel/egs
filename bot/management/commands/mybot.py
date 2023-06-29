from django.core.management.base import BaseCommand
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater
from telegram.utils.request import Request

from bot.models import TelegramUsers
from core.models import Employees

from egs.settings import TOKEN

def log_errors(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {str(e)}'
            print(error_message)
            raise e
    return inner

# @log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    keyboard = [[KeyboardButton(text='Поделиться контактом',
                                 request_contact=True),]]
    user = None
    try:
        user = TelegramUsers.objects.get(chat_id=chat_id)
    except:
        pass

    if user:
        update.message.reply_text(text=f'Вы уже зарегестрированы, {user.name}',
                                  reply_markup=ReplyKeyboardMarkup(keyboard))
    else:
        update.message.reply_text(text='Привет, чтобы начать пользоваться ботом, поделитесь контактом',
                                  reply_markup=ReplyKeyboardMarkup(keyboard))


@log_errors
def get_contact(update: Update, context: CallbackContext):
    contact = update.message.contact

    user = None
    try:
        user = Employees.objects.get(phone=contact.phone_number)
    except:
        pass

    if user:
        TelegramUsers.objects.update_or_create(
            name=contact.first_name,
            surname=contact.last_name,
            chat_id=update.message.chat_id,
            phone_number=contact.phone_number
        )
        update.message.reply_text(text='Вы успешно зарегестрированы')
    else:
        update.message.reply_text(text='Данного номера нет в моих списках :(')

class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        request = Request(connect_timeout=0.5, read_timeout=1.0, con_pool_size=8)

        bot = Bot(request=request, token=TOKEN)

        print(bot.get_me())

        updater = Updater(bot=bot, use_context=True)

        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)
        updater.dispatcher.add_handler(MessageHandler(Filters.contact, get_contact))

        updater.start_polling()
        updater.idle()

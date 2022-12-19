from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# https://t.me/pdpmega228_bot
token = "5473058261:AAG3cKwP6k3hYdxXfrzIkZcwuA70e98i2ms"
bot = Bot(token)
dispatcher = Dispatcher(bot)

helpText = "/help - список комманд\n" \
           "/start - начать работу\n" \
           "/photo - отправляет смешной прикол\n" \
           "/advice - дает совет"

a = InlineKeyboardButton(text='Ссылка на отчисление', url='https://www.hse.ru/ba/ami/rqsts?ysclid=lbqnn0p9zv763228333')
b = InlineKeyboardButton(text='Ссылка на wiki', url='http://wiki.cs.hse.ru/Wiki_ФКН')
button = InlineKeyboardMarkup()
button.add(a, b)


@dispatcher.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуй, друг. Напиши /help, чтобы увидеть функционал бота.')


@dispatcher.message_handler(commands=['help'])
async def help_com(message: types.Message):
    await message.reply(text=helpText)


@dispatcher.message_handler(commands=['photo'])
async def photo(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://ne-kurim.ru/forum/attachments/qsgmjtocssk-jpg.1061830/')


@dispatcher.message_handler(commands=['advice'])
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, text='Беги, глупец', reply_markup=button)


@dispatcher.message_handler()
async def echo(message: types.Message):
    await message.answer(text="Ты написал что-то не то, напиши /help, чтобы узнать существующие комманды")
    await bot.send_message(message.from_user.id, text="Отправляю тебе обратно твое сообщение!")
    await bot.send_message(message.from_user.id, text=message.text.upper())


def main():
    executor.start_polling(dispatcher)


if __name__ == "__main__":
    main()



from aiogram import types , Dispatcher
from coin import bot, dp



# @dp.message_handler()
async def echo(message: types.Message):
    jj = message.text
    if type(jj) == type(456):
        daff = jj * jj
        await bot.send_message(message.from_user.id, daff)

    elif type(jj) == type('hukb'):
        await bot.send_message(message.from_user.id, message.text)

def register_handler_ezta(dp: Dispatcher):
    dp.register_message_handler(echo, content_types='qretwuci456vhthc4er')











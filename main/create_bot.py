from aiogram import Bot
from aiogram.dispatcher import Dispatcher

TOKEN = '6131780236:AAFf3ddaFkl7CSs3DkfXyI6u6KaKWMz3Cbo'  # уникальный код бота

bot = Bot(token=TOKEN)  # инициализируем бота
dp = Dispatcher(bot)  # инициализируем диспетчер (чтобы следить за обновлениями (???))

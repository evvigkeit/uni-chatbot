from aiogram import executor, types

from main.create_bot import dp
from handlers import literature, brv, teacher_info, schedule

brv.register_handlers_brv(dp)
schedule.register_handlers_schedule(dp)
literature.register_handlers_literature(dp)
teacher_info.register_handlers_teachers(dp)


'''******************************* СТАРТ **********************************'''


async def on_startup(_):
    # bases.base_links_start()
    print('success!')


# 'имя диспетчера'.message_handler() - Декоратор для редактируемого обработчика сообщений (здесь - списка команд)
@dp.message_handler(commands=['start', 'help'])
# async def: до момента вызова ф-ий `/start` или `/help` бот находится в режиме ожидания
# message: - параметр, в который приходит сообщение из декоратора; название можно дать любое
# types.Message - Этот объект представляет собой сообщение.
async def welcome(message: types.Message):
    # await: в процессе ожидания ответа бот продолжает работу
    await message.answer('''Ниже указан список доступных команд 😎:

/schedule - отправляет ссылки на расписание занятий 📆

/brv - отправляет ссылки на балльно-рейтинговые ведомости 😋

/literature - отправляет ссылки на учебно-методические материалы по дисциплинам 📕

/teachers - отправляет адреса электронных почт преподавателей 🙋''')


'''***************************** НЕВЕРНАЯ КОМАНДА **************************************'''


@dp.message_handler()
async def empty(message: types.Message):
    await message.answer('''Извините, данная команда мне непонятна 🥲
    
Попрубуйте выбрать из списка доступных команд 🤔:

/schedule - отправляет ссылки на расписание занятий 📆

/brv - отправляет ссылки на балльно-рейтинговые ведомости 😋

/literature - отправляет ссылки на учебно-методические материалы по дисциплинам 📕

/teachers - отправляет адреса электронных почт преподавателей 🙋''')


if __name__ == '__main__':
    # executor.start_polling - Запустить бота в режиме длительного опроса
    executor.start_polling(dp, on_startup=on_startup)

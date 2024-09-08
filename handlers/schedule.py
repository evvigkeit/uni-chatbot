from aiogram import Dispatcher, types
from main.create_bot import bot


async def schedule_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    full_sch = types.InlineKeyboardButton(text="Очная", url='https://reu.by/studentam/raspisanie-ofo.html')
    dist_sch = types.InlineKeyboardButton(text="Заочная", url="https://reu.by/studentam/raspisanie-zfo.html")
    teach_sch = types.InlineKeyboardButton(text="Преподователей", url="https://reu.by/studentam/raspisanie-prep.html")
    evening_sch = types.InlineKeyboardButton(text="Очно-заочная", url="https://reu.by/studentam/raspisanie-ozfo.html")
    masters_sch = types.InlineKeyboardButton(text="Магистратура", url="https://reu.by/studentam/raspisanie-mag.html")
    course_sch = types.InlineKeyboardButton(text="Повышение квалификации",
                                            url="https://reu.by/studentam/raspisanie-zanyatij-kursy-povysheniya"
                                                "-kvalifikatsii.html")
    back = types.InlineKeyboardButton(text='⬅️Назад', callback_data='back')
    keyboard.row(full_sch, evening_sch)
    keyboard.row(masters_sch, teach_sch)
    keyboard.row(dist_sch, course_sch)
    keyboard.row(back)
    await bot.send_message(message.chat.id, "Расписание можно посмотреть по ссылкам:", reply_markup=keyboard)


# @dp.callback_query_handler(text='back')
async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.answer('''Ниже указан список доступных команд 😎:

/schedule - отправляет ссылки на расписание занятий 📆

/brv - отправляет ссылки на бально-рейтинговые ведомости 😋

/literature - отправляет ссылки на учебно-методические материалы по дисциплинам 📕

/teachers - отправляет адреса электронных почт преподавателей 🙋''')
    await callback.message.delete()


def register_handlers_schedule(dp: Dispatcher):
    dp.register_message_handler(schedule_command, commands=['schedule'])
    dp.register_callback_query_handler(back_to_menu, text='back')

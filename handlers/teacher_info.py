from aiogram import Dispatcher, types
from main import bases
from main.create_bot import bot, dp
from handlers import schedule

bases.base_start()
base_m = bases.base_teachers_management_answer()
base_it = bases.base_teachers_it_answer()
schedule.register_handlers_schedule(dp)


'''********************* ВЫБОР ФОРМЫ ОБУЧЕНИЯ *******************************************'''


async def cafedra_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    management = types.InlineKeyboardButton(text="Кафедра менеджмента, учета и финансов", callback_data='management')
    technology = types.InlineKeyboardButton(text="Кафедра ИТ и социально-гуманитарных дисциплин",
                                            callback_data='it')
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='back')
    keyboard.row(management)
    keyboard.row(technology)
    keyboard.row(back)
    await bot.send_message(message.chat.id, "Выберите кафедру, на которой числится преподаватель:",
                           reply_markup=keyboard)


'''********************* КАФЕДРА МЕНЕДЖМЕНТА И УЧЕТА ФИНАНСОВ *******************************************'''


async def management_options(callback: types.CallbackQuery):
    await callback.message.answer(f'''Ниже указана информация о преподователях кафедры менеджмента и учета финансов:
    
- {base_m[0][0]} 
email  ✉: {base_m[0][1]}
- {base_m[1][0]} 
email  ✉: {base_m[1][1]}
- {base_m[2][0]} 
email  ✉: {base_m[2][1]}
- {base_m[3][0]} 
email  ✉: {base_m[3][1]}
- {base_m[4][0]} 
email  ✉: {base_m[4][1]}
- {base_m[5][0]} 
email  ✉: {base_m[5][1]}
- {base_m[6][0]} 
email  ✉: {base_m[6][1]}
- {base_m[7][0]} 
email  ✉: {base_m[7][1]}
- {base_m[8][0]} 
email  ✉: {base_m[8][1]}
- {base_m[9][0]} 
email  ✉: {base_m[9][1]}
- {base_m[10][0]}
email  ✉: {base_m[10][1]}
- {base_m[11][0]}
email  ✉: {base_m[11][1]}
- {base_m[12][0]} 
email  ✉: {base_m[12][1]}
- {base_m[13][0]} 
email  ✉: {base_m[13][1]}
- {base_m[14][0]} 
email  ✉: {base_m[14][1]}
''')
    await callback.message.delete()


'''********************* КАФЕДРА МЕНЕДЖМЕНТА ИT *******************************************'''


async def it_options(callback: types.CallbackQuery):
    await callback.message.answer(f'''Ниже указана информация о преподователях кафедры ИТ и социально-гуманитарных дисциплин: 

- {base_it[0][0]} 
email  ✉: {base_it[0][1]}
- {base_it[1][0]} 
email  ✉: {base_it[1][1]}
- {base_it[2][0]} 
email  ✉: {base_it[2][1]}
- {base_it[3][0]} 
email  ✉: {base_it[3][1]}
- {base_it[4][0]} 
email  ✉: {base_it[4][1]}
- {base_it[5][0]} 
email  ✉: {base_it[5][1]}
- {base_it[6][0]} 
email  ✉: {base_it[6][1]}
- {base_it[7][0]} 
email  ✉: {base_it[7][1]}
- {base_it[8][0]} 
email  ✉: {base_it[8][1]}
''')
    await callback.message.delete()


def register_handlers_teachers(dp: Dispatcher):
    dp.register_message_handler(cafedra_command, commands=['teachers'])
    dp.register_callback_query_handler(management_options, text='management')
    dp.register_callback_query_handler(it_options, text='it')

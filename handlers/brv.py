from aiogram import Dispatcher, types
from main import bases
from main.create_bot import bot, dp
from handlers import schedule

bases.base_start()
base_l = bases.base_links_answer()
schedule.register_handlers_schedule(dp)


'''********************* ВЫБОР ФОРМЫ ОБУЧЕНИЯ *******************************************'''


# @dp.message_handler(commands=['brv'])
async def brv_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    full_brv = types.InlineKeyboardButton(text="Очная", callback_data='full_brv')
    dist_brv = types.InlineKeyboardButton(text="Заочная", callback_data='dist_brv')
    masters_brv = types.InlineKeyboardButton(text="Магистратура", url='https://drive.google.com/drive/folders'
                                                                      '/1Fifz6O81wpzeRokBWLnlE0VtsEwY-e5Z')
    evening_brv = types.InlineKeyboardButton(text="Очно-заочная", callback_data='evening_brv')
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='back')
    keyboard.row(full_brv, dist_brv)
    keyboard.row(evening_brv, masters_brv)
    keyboard.row(back)
    await bot.send_message(message.chat.id, "Выберите форму обучения:", reply_markup=keyboard)


'''***************** ОПЦИИ ДЛЯ ОЧНОЙ ФОРМЫ ОБУЧЕНИЯ ******************************'''


async def full_brv_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    full_dkm_brv = types.InlineKeyboardButton(text='Бизнес-информатика', callback_data='full_dkm_brv')
    full_dme_brv = types.InlineKeyboardButton(text='Менеджмент', callback_data='full_dme_brv')
    full_dee_brv = types.InlineKeyboardButton(text='Экономика', callback_data='full_dee_brv')
    keyboard.row(full_dme_brv, full_dee_brv)
    keyboard.row(full_dkm_brv)
    await callback.message.answer('Выберите образовательную программу:', reply_markup=keyboard)
    await callback.message.delete()


'''********************* ОПЦИИ ДЛЯ ОЧНОЙ ФОРМЫ ГРУПП МИ-ДКМ ****************************'''


async def full_dkm_brv_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    brv_dkm_211 = types.InlineKeyboardButton(text=base_l[0][0], url=base_l[0][1])
    brv_dkm_221 = types.InlineKeyboardButton(text=base_l[1][0], url=base_l[1][1])
    brv_dkm_222 = types.InlineKeyboardButton(text=base_l[2][0], url=base_l[2][1])
    brv_dkm_201 = types.InlineKeyboardButton(text=base_l[3][0], url=base_l[3][1])
    brv_dkm_801 = types.InlineKeyboardButton(text=base_l[4][0], url=base_l[4][1])
    brv_dkm_901 = types.InlineKeyboardButton(text=base_l[5][0], url=base_l[5][1])
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='full_brv')
    keyboard.row(brv_dkm_211, brv_dkm_221)
    keyboard.row(brv_dkm_222, brv_dkm_201)
    keyboard.row(brv_dkm_801, brv_dkm_901)
    keyboard.row(back)
    await callback.message.answer('Ниже указаны ссылки на балльно-рейтенговые ведомости по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''**************** ОПЦИИ ДЛЯ ОЧНОЙ ФОРМЫ ГРУПП МИ-ДМЕ *****************************'''


async def full_dme_brv_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    brv_dme_211 = types.InlineKeyboardButton(text=base_l[6][0], url=base_l[6][1])
    brv_dme_221 = types.InlineKeyboardButton(text=base_l[7][0], url=base_l[7][1])
    brv_dme_201 = types.InlineKeyboardButton(text=base_l[8][0], url=base_l[8][1])
    brv_dme_801 = types.InlineKeyboardButton(text=base_l[10][0], url=base_l[10][1])
    brv_dme_901 = types.InlineKeyboardButton(text=base_l[11][0], url=base_l[11][1])
    back_to_full_brv = types.InlineKeyboardButton(text="⬅️Назад", callback_data='full_brv')
    keyboard.row(brv_dme_211, brv_dme_221)
    keyboard.row(brv_dme_201, brv_dme_801)
    keyboard.row(brv_dme_901)
    keyboard.row(back_to_full_brv)
    await callback.message.answer('Ниже указаны ссылки на балльно-рейтенговые ведомости по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''**************** ОПЦИИ ДЛЯ ОЧНОЙ ФОРМЫ ГРУПП МИ-ДЭЭ *****************************'''


async def full_dee_brv_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    brv_dee_211 = types.InlineKeyboardButton(text=base_l[12][0], url=base_l[12][1])
    brv_dee_221 = types.InlineKeyboardButton(text=base_l[13][0], url=base_l[13][1])
    back_to_full_brv = types.InlineKeyboardButton(text="⬅️Назад", callback_data='full_brv')
    keyboard.row(brv_dee_211, brv_dee_221)
    keyboard.row(back_to_full_brv)
    await callback.message.answer('Ниже указаны ссылки на балльно-рейтенговые ведомости по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''***************** ОПЦИИ ДЛЯ ЗАОЧНОЙ ФОРМЫ ОБУЧЕНИЯ ******************************'''


async def dist_brv_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    zkm_brv = types.InlineKeyboardButton(text='Ми-ЗКМ', callback_data='zkm_brv')
    zme_brv = types.InlineKeyboardButton(text='Ми-ЗМЕ', callback_data='zme_brv')
    zee_brv = types.InlineKeyboardButton(text='Ми-ЗЭЭ', callback_data='zee_brv')
    keyboard.row(zkm_brv, zme_brv, zee_brv)
    await callback.message.answer('Выберите образовательную программу:', reply_markup=keyboard)
    await callback.message.delete()


'''********************* ОПЦИИ ДЛЯ ГРУПП МИ-ЗКМ ****************************'''


async def zkm_brv_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    brv_zkm_701 = types.InlineKeyboardButton(text=base_l[14][0], url=base_l[14][1])
    brv_zkm_201 = types.InlineKeyboardButton(text=base_l[15][0], url=base_l[15][1])
    brv_zkm_801 = types.InlineKeyboardButton(text=base_l[16][0], url=base_l[16][1])
    brv_zkm_901 = types.InlineKeyboardButton(text=base_l[17][0], url=base_l[17][1])
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='dist_brv')
    keyboard.row(brv_zkm_201, brv_zkm_701)
    keyboard.row(brv_zkm_801, brv_zkm_901)
    keyboard.row(back)
    await callback.message.answer('Ниже указаны ссылки на балльно-рейтенговые ведомости по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''********************* ОПЦИИ ДЛЯ ГРУПП МИ-ЗМЕ ****************************'''


async def zme_brv_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    brv_zme_20x = types.InlineKeyboardButton(text=base_l[19][0], url=base_l[19][1])
    brv_zme_70 = types.InlineKeyboardButton(text=base_l[20][0], url=base_l[20][1])
    brv_zme_80x = types.InlineKeyboardButton(text=base_l[21][0], url=base_l[21][1])
    brv_zme_90x = types.InlineKeyboardButton(text=base_l[22][0], url=base_l[22][1])
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='dist_brv')
    keyboard.row(brv_zme_20x, brv_zme_70)
    keyboard.row(brv_zme_80x, brv_zme_90x)
    keyboard.row(back)
    await callback.message.answer('Ниже указаны ссылки на балльно-рейтенговые ведомости по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''********************* ОПЦИИ ДЛЯ ГРУПП МИ-ЗЭЭ ****************************'''


async def zee_brv_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    brv_zee_201 = types.InlineKeyboardButton(text=base_l[24][0], url=base_l[24][1])
    brv_zee_701 = types.InlineKeyboardButton(text=base_l[25][0], url=base_l[25][1])
    brv_zee_801_2 = types.InlineKeyboardButton(text=base_l[26][0], url=base_l[26][1])
    brv_zee_901 = types.InlineKeyboardButton(text=base_l[27][0], url=base_l[27][1])
    brv_zee_801 = types.InlineKeyboardButton(text=base_l[28][0], url=base_l[28][1])
    brv_zee_802 = types.InlineKeyboardButton(text=base_l[29][0], url=base_l[29][1])
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='dist_brv')
    keyboard.row(brv_zee_201, brv_zee_701)
    keyboard.row(brv_zee_801_2, brv_zee_901)
    keyboard.row(brv_zee_801, brv_zee_802)
    keyboard.row(back)
    await callback.message.answer('Ниже указаны ссылки на балльно-рейтенговые ведомости по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''***************** ОПЦИИ ДЛЯ ВЕЧЕРНЕЙ ФОРМЫ ОБУЧЕНИЯ ******************************'''


async def evening_brv_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    brv_o_zkm_221 = types.InlineKeyboardButton(text=base_l[33][0], url=base_l[33][1])
    brv_ozm_211 = types.InlineKeyboardButton(text=base_l[34][0], url=base_l[34][1])
    brv_ozm_901 = types.InlineKeyboardButton(text=base_l[35][0], url=base_l[35][1])
    keyboard.row(brv_o_zkm_221, brv_ozm_211)
    keyboard.row(brv_ozm_901)
    await callback.message.answer('Ниже указаны ссылки на балльно-рейтенговые ведомости по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


def register_handlers_brv(dp: Dispatcher):
    dp.register_message_handler(brv_command, commands=['brv'])
    dp.register_callback_query_handler(full_brv_options, text='full_brv')
    dp.register_callback_query_handler(dist_brv_options, text='dist_brv')
    dp.register_callback_query_handler(evening_brv_options, text='evening_brv')
    dp.register_callback_query_handler(full_dkm_brv_options, text='full_dkm_brv')
    dp.register_callback_query_handler(full_dme_brv_options, text='full_dme_brv')
    dp.register_callback_query_handler(full_dee_brv_options, text='full_dee_brv')
    dp.register_callback_query_handler(zkm_brv_options, text='zkm_brv')
    dp.register_callback_query_handler(zme_brv_options, text='zme_brv')
    dp.register_callback_query_handler(zee_brv_options, text='zee_brv')

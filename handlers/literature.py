from aiogram import Dispatcher, types
from main.create_bot import bot, dp
from main import bases
from handlers import schedule

bases.base_start()
base_l = bases.base_links_answer()
schedule.register_handlers_schedule(dp)

'''********************* ВЫБОР ФОРМЫ ОБУЧЕНИЯ *******************************************'''


async def literature_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    full_lit = types.InlineKeyboardButton(text="Очная", callback_data='full_lit')
    dist_lit = types.InlineKeyboardButton(text="Заочная", callback_data='dist_lit')
    masters_lit = types.InlineKeyboardButton(text="Магистратура", callback_data='masters_lit')
    evening_lit = types.InlineKeyboardButton(text="Очно-заочная", callback_data='evening_lit')
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='back')
    keyboard.row(full_lit, dist_lit)
    keyboard.row(evening_lit, masters_lit)
    keyboard.row(back)
    await bot.send_message(message.chat.id, "Выберите форму обучения:", reply_markup=keyboard)


'''***************** ОПЦИИ ДЛЯ ОЧНОЙ ФОРМЫ ОБУЧЕНИЯ ******************************'''


async def full_lit_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    full_dkm_lit = types.InlineKeyboardButton(text='Бизнес-информатика', callback_data='full_dkm_lit')
    full_dme_lit = types.InlineKeyboardButton(text='Менеджмент', callback_data='full_dme_lit')
    full_dee_lit = types.InlineKeyboardButton(text='Экономика', callback_data='full_dee_lit')
    keyboard.row(full_dme_lit, full_dee_lit)
    keyboard.row(full_dkm_lit)
    await callback.message.answer('Выберите образовательную программу:', reply_markup=keyboard)
    await callback.message.delete()


'''********************* ОПЦИИ ДЛЯ ОЧНОЙ ФОРМЫ ГРУПП МИ-ДКМ ****************************'''


async def full_dkm_lit_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    lit_22_23_dkm_211 = types.InlineKeyboardButton(text=base_l[0][0], url=base_l[0][2])
    lit_22_23_dkm_221 = types.InlineKeyboardButton(text=base_l[1][0], url=base_l[1][2])
    lit_22_23_dkm_201 = types.InlineKeyboardButton(text=base_l[3][0], url=base_l[3][2])
    lit_22_23_dkm_901 = types.InlineKeyboardButton(text=base_l[5][0], url=base_l[5][2])
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='full_lit')
    keyboard.row(lit_22_23_dkm_211, lit_22_23_dkm_221)
    keyboard.row(lit_22_23_dkm_201, lit_22_23_dkm_901)
    keyboard.row(back)
    await callback.message.answer('Ниже указаны ссылки на учебно-методические материалы по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''**************** ОПЦИИ ДЛЯ ОЧНОЙ ФОРМЫ ГРУПП МИ-ДМЕ *****************************'''


async def full_dme_lit_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    lit_dme_211 = types.InlineKeyboardButton(text=base_l[6][0], url=base_l[6][2])
    lit_dme_221 = types.InlineKeyboardButton(text=base_l[7][0], url=base_l[7][2])
    lit_dme_201 = types.InlineKeyboardButton(text=base_l[8][0], url=base_l[8][2])
    lit_dme_701 = types.InlineKeyboardButton(text=base_l[9][0], url=base_l[9][2])
    lit_dme_801 = types.InlineKeyboardButton(text=base_l[10][0], url=base_l[10][2])
    lit_dme_901 = types.InlineKeyboardButton(text=base_l[11][0], url=base_l[11][2])
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='full_lit')
    keyboard.row(lit_dme_211, lit_dme_221)
    keyboard.row(lit_dme_201, lit_dme_701)
    keyboard.row(lit_dme_801, lit_dme_901)
    keyboard.row(back)
    await callback.message.answer('Ниже указаны ссылки на учебно-методические материалы по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''**************** ОПЦИИ ДЛЯ ОЧНОЙ ФОРМЫ ГРУПП МИ-ДЭЭ *****************************'''


async def full_dee_lit_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    lit_dee_211 = types.InlineKeyboardButton(text=base_l[12][0], url=base_l[12][2])
    lit_dee_221 = types.InlineKeyboardButton(text=base_l[13][0], url=base_l[13][2])
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='full_lit')
    keyboard.row(lit_dee_211, lit_dee_221)
    keyboard.row(back)
    await callback.message.answer('Ниже указаны ссылки на учебно-методические материалы по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''***************** ОПЦИИ ДЛЯ ЗАОЧНОЙ ФОРМЫ ОБУЧЕНИЯ ******************************'''


async def dist_lit_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    zkm_lit = types.InlineKeyboardButton(text='Ми-ЗКМ', callback_data='zkm_lit')
    zme_lit = types.InlineKeyboardButton(text='Ми-ЗМЕ', callback_data='zme_lit')
    zee_lit = types.InlineKeyboardButton(text='Ми-ЗЭЭ', callback_data='zee_lit')
    keyboard.row(zkm_lit, zme_lit, zee_lit)
    await callback.message.answer('Выберите образовательную программу:', reply_markup=keyboard)
    await callback.message.delete()


'''********************* ОПЦИИ ДЛЯ ГРУПП МИ-ЗКМ ****************************'''


async def zkm_lit_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    lit_zkm_701 = types.InlineKeyboardButton(text=base_l[14][0], url=base_l[14][2])
    lit_zkm_201 = types.InlineKeyboardButton(text=base_l[15][0], url=base_l[15][2])
    lit_zkm_801 = types.InlineKeyboardButton(text=base_l[16][0], url=base_l[16][2])
    lit_zkm_901 = types.InlineKeyboardButton(text=base_l[17][0], url=base_l[17][2])
    lit_zkm_601 = types.InlineKeyboardButton(text=base_l[18][0], url=base_l[18][2])
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='dist_lit')
    keyboard.row(lit_zkm_201, lit_zkm_701)
    keyboard.row(lit_zkm_801, lit_zkm_901)
    keyboard.row(lit_zkm_601)
    keyboard.row(back)
    await callback.message.answer('Ниже указаны ссылки на учебно-методические материалы по группам:',
                                  reply_markup=keyboard)
    # await callback.message.delete()


'''********************* ОПЦИИ ДЛЯ ГРУПП МИ-ЗМЕ ****************************'''


async def zme_lit_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    lit_zme_20x = types.InlineKeyboardButton(text=base_l[19][0], url=base_l[19][2])
    lit_zme_70 = types.InlineKeyboardButton(text=base_l[20][0], url=base_l[20][2])
    lit_zme_80x = types.InlineKeyboardButton(text=base_l[21][0], url=base_l[21][2])
    lit_zme_90x = types.InlineKeyboardButton(text=base_l[22][0], url=base_l[22][2])
    lit_zme_60x = types.InlineKeyboardButton(text=base_l[23][0], url=base_l[23][2])
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='dist_lit')
    keyboard.row(lit_zme_20x, lit_zme_70)
    keyboard.row(lit_zme_80x, lit_zme_90x)
    keyboard.row(lit_zme_60x)
    keyboard.row(back)
    await callback.message.answer('Ниже указаны ссылки на учебно-методические материалы по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''********************* ОПЦИИ ДЛЯ ГРУПП МИ-ЗЭЭ ****************************'''


async def zee_lit_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    zee_201 = types.InlineKeyboardButton(text=base_l[24][0], url=base_l[24][2])
    zee_901 = types.InlineKeyboardButton(text=base_l[27][0], url=base_l[27][2])
    zee_70x = types.InlineKeyboardButton(text=base_l[30][0], url=base_l[30][2])
    zee_80x = types.InlineKeyboardButton(text=base_l[31][0], url=base_l[31][2])
    zee_60x = types.InlineKeyboardButton(text=base_l[32][0], url=base_l[32][2])
    back = types.InlineKeyboardButton(text="⬅️Назад", callback_data='dist_lit')
    keyboard.row(zee_201, zee_70x)
    keyboard.row(zee_80x, zee_901)
    keyboard.row(zee_60x)
    keyboard.row(back)
    await callback.message.answer('Ниже указаны ссылки на учебно-методические материалы по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''***************** ОПЦИИ ДЛЯ ВЕЧЕРНЕЙ ФОРМЫ ОБУЧЕНИЯ ******************************'''


async def evening_lit_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    o_zkm_221 = types.InlineKeyboardButton(text=base_l[33][0], url=base_l[33][2])
    ozm_211 = types.InlineKeyboardButton(text=base_l[34][0], url=base_l[34][2])
    ozm_901 = types.InlineKeyboardButton(text=base_l[35][0], url=base_l[35][2])
    keyboard.row(o_zkm_221, ozm_211, ozm_901)
    await callback.message.answer('Ниже указаны ссылки на учебно-методические материалы по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


'''***************** ОПЦИИ ДЛЯ МАГИСТРАТУРЫ ******************************'''


async def masters_lit_options(callback: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    zeje_221 = types.InlineKeyboardButton(text=base_l[36][0], url=base_l[36][2])
    zeje_211 = types.InlineKeyboardButton(text=base_l[37][0], url=base_l[37][2])
    zeje = types.InlineKeyboardButton(text=base_l[38][0], url=base_l[38][2])
    zmo = types.InlineKeyboardButton(text=base_l[39][0], url=base_l[39][2])
    keyboard.row(zeje_221, zeje_211)
    keyboard.row(zeje, zmo)
    await callback.message.answer('Ниже указаны ссылки на учебно-методические материалы по группам:',
                                  reply_markup=keyboard)
    await callback.message.delete()


def register_handlers_literature(dp: Dispatcher):
    dp.register_message_handler(literature_command, commands=['literature'])

    dp.register_callback_query_handler(full_lit_options, text='full_lit')
    dp.register_callback_query_handler(full_dkm_lit_options, text='full_dkm_lit')
    dp.register_callback_query_handler(dist_lit_options, text='dist_lit')
    dp.register_callback_query_handler(full_dme_lit_options, text='full_dme_lit')
    dp.register_callback_query_handler(full_dee_lit_options, text='full_dee_lit')
    dp.register_callback_query_handler(zkm_lit_options, text='zkm_lit')
    dp.register_callback_query_handler(zme_lit_options, text='zme_lit')
    dp.register_callback_query_handler(zee_lit_options, text='zee_lit')
    dp.register_callback_query_handler(evening_lit_options, text='evening_lit')
    dp.register_callback_query_handler(masters_lit_options, text='masters_lit')

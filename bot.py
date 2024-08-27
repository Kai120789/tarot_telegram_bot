import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from functions.one_card import one_card
from functions.three_cards import three_cards
from functions.five_cards import five_cards
from functions.six_cards import six_cards
from functions.seven_cards import seven_cards
from functions.eight_cards import eight_cards
from functions.ten_cards import ten_cards
from aiogram.enums import ParseMode
from db_create_connect_fill.connection import connToDb
import os
from fate_matrix import fate_matrix
from dotenv import load_dotenv


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
load_dotenv()
token = os.getenv("BOT_TOKEN")
bot = Bot(token=token)
# Диспетчер
dp = Dispatcher()

file_ids = []

last_user_msg = ''

""" class Form(StatesGroup):
    waiting_for_birthdate = State() """

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Гадание на Таро")],
        [types.KeyboardButton(text="Матрица судьбы")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    global last_user_msg
    last_user_msg = ''
    await message.answer("Что хотите попробовать?", reply_markup=keyboard)
    """ file_ids = []
    image_from_pc = FSInputFile(f"img/0{1}.jpeg")
    result = await message.answer_photo(
        image_from_pc
    )
    file_ids.append(result.photo[-1].file_id) """

# возврат на начало меню   
@dp.message(F.text.lower() == "вернуться")
async def re_turn(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Гадание на Таро")],
        [types.KeyboardButton(text="Матрица судьбы")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    global last_user_msg
    last_user_msg = ''
    await message.answer("Что хотите попробовать?", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "гадание на таро")
async def tarot(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Выложить 1 карту")],
        [types.KeyboardButton(text="Сделать расклад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("Отличный выбор", reply_markup=keyboard)

@dp.message(F.text.lower() == "матрица судьбы")
async def tarot(message: types.Message):
    global last_user_msg
    last_user_msg = message.text
    await message.reply("Введите дату рождения в формате (ДД.ММ.ГГГГ)")
    

# выложить 1 карту
@dp.message(F.text.lower() == "выложить 1 карту")
async def tarot_one(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Карта дня")],
        [types.KeyboardButton(text="Карта месяца")],
        [types.KeyboardButton(text="Совет карты")],
        [types.KeyboardButton(text="Да/Нет")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("Выберите категорию", reply_markup=keyboard)

# карта дня
@dp.message(F.text.lower() == "карта дня")
async def tarot_one_day_card(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Повторить (карта дня)")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, res, n = one_card('card_text_day_card')
    s = "img/"+str(n)+".jpeg"
    image_from_pc = FSInputFile(s)
    result = await message.answer_photo(
        image_from_pc,
        caption=f"<b>{cards_up[0]}</b>\n{res}",
        parse_mode=ParseMode.HTML, 
        reply_markup=keyboard
    )
    file_ids.append(result.photo[-1].file_id)
    #await message.answer(f"{cards_up[0]}\n{res}".join(file_ids), reply_markup=keyboard)
    #await message.answer(f"{cards_up[0]}\n{res}")
    
@dp.message(F.text.lower() == "повторить (карта дня)")
async def tarot(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Повторить (карта дня)")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, res, n = one_card('card_text_day_card')
    s = "img/"+str(n)+".jpeg"
    image_from_pc = FSInputFile(s)
    result = await message.answer_photo(
        image_from_pc,
        caption=f"<b>{cards_up[0]}</b>\n{res}",
        parse_mode=ParseMode.HTML,  
        reply_markup=keyboard
    )
    file_ids.append(result.photo[-1].file_id)
    #await message.answer(f"{cards_up[0]}\n{res}", reply_markup=keyboard)

# карта месяца
@dp.message(F.text.lower() == "карта месяца")
async def tarot(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Повторить (карта месяца)")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, res, n = one_card('card_text_month')
    res = res[:res.index("На месяц в любви")]
    s = "img/"+str(n)+".jpeg"
    image_from_pc = FSInputFile(s)
    result = await message.answer_photo(
        image_from_pc,
        caption=f"<b>{cards_up[0]}</b>\n{res}",
        parse_mode=ParseMode.HTML,  
        reply_markup=keyboard
    )
    file_ids.append(result.photo[-1].file_id)
    #await message.answer(f"{cards_up[0]}\n{res}", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "повторить (карта месяца)")
async def tarot(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Повторить (карта месяца)")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, res, n = one_card('card_text_month')
    res = res[:res.index("На месяц в любви")]
    s = "img/"+str(n)+".jpeg"
    image_from_pc = FSInputFile(s)
    result = await message.answer_photo(
        image_from_pc,
        caption=f"<b>{cards_up[0]}</b>\n{res}",
        parse_mode=ParseMode.HTML,  
        reply_markup=keyboard
    )
    file_ids.append(result.photo[-1].file_id)
    #await message.answer(f"{cards_up[0]}\n{res}", reply_markup=keyboard)    

# совет карты
@dp.message(F.text.lower() == "совет карты")
async def tarot(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Повторить (совет карты)")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, res, n = one_card('card_text_sovet')
    s = "img/"+str(n)+".jpeg"
    image_from_pc = FSInputFile(s)
    result = await message.answer_photo(
        image_from_pc,
        caption=f"<b>{cards_up[0]}</b>\n{res}",
        parse_mode=ParseMode.HTML, 
        reply_markup=keyboard
    )
    file_ids.append(result.photo[-1].file_id)
    #await message.answer(f"{cards_up[0]}\n{res}", reply_markup=keyboard)
    
@dp.message(F.text.lower() == "повторить (совет карты)")
async def tarot(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Повторить (совет карты)")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, res, n = one_card('card_text_sovet')
    s = "img/"+str(n)+".jpeg"
    image_from_pc = FSInputFile(s)
    result = await message.answer_photo(
        image_from_pc,
        caption=f"<b>{cards_up[0]}</b>\n{res}",
        parse_mode=ParseMode.HTML,  
        reply_markup=keyboard
    )
    file_ids.append(result.photo[-1].file_id)
    #await message.answer(f"{cards_up[0]}\n{res}", reply_markup=keyboard)

# да/нет
@dp.message(F.text.lower() == "да/нет")
async def cmd_start(message: types.Message):
    kb = [
    [types.KeyboardButton(text="Повторить (да/нет)")],
    [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, res, n = one_card('card_text_yes_or_no')
    s = "img/"+str(n)+".jpeg"
    image_from_pc = FSInputFile(s)
    result = await message.answer_photo(
        image_from_pc,
        caption=f"<b>{cards_up[0]}</b>\n{res}",
        parse_mode=ParseMode.HTML, 
        reply_markup=keyboard
    )
    file_ids.append(result.photo[-1].file_id)
    #await message.answer(f"{cards_up[0]}\n{res}", reply_markup=keyboard)

    
@dp.message(F.text.lower() == "повторить (да/нет)")
async def cmd_start(message: types.Message):
    kb = [
    [types.KeyboardButton(text="Повторить (да/нет)")],
    [types.KeyboardButton(text="Вернуться")]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, res, n = one_card('card_text_yes_or_no')
    s = "img/"+str(n)+".jpeg"
    image_from_pc = FSInputFile(s)
    result = await message.answer_photo(
        image_from_pc,
        caption=f"<b>{cards_up[0]}</b>\n{res}",
        parse_mode=ParseMode.HTML, 
        reply_markup=keyboard
    )
    file_ids.append(result.photo[-1].file_id)
    #await message.answer(f"{cards_up[0]}\n{res}", reply_markup=keyboard)    

# 3+ карт
@dp.message(F.text.lower() == "сделать расклад")
async def tarot_three_plus(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Обычный")],
        [types.KeyboardButton(text="Любовь и отношения")],
        [types.KeyboardButton(text="Ситуация и вопрос")],
        [types.KeyboardButton(text="Работа и финансы")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("Выберите категорию", reply_markup=keyboard)

# обычные значения
@dp.message(F.text.lower() == "обычный")
async def tarot_three_plus(message: types.Message):
    kb = [
        [types.KeyboardButton(text="обычный 3 карты")],
        [types.KeyboardButton(text="обычный 5 карт")],
        [types.KeyboardButton(text="обычный 8 карт")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("Выберите количество карт", reply_markup=keyboard)

# обычные значения 3
@dp.message(F.text.lower() == "обычный 3 карты")
async def tarot_camon_three(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Разум, тело, душа")],
        [types.KeyboardButton(text="Состояние")],
        [types.KeyboardButton(text="Прошлое, настоящее, будущее")],
        [types.KeyboardButton(text="Мысли и чувства")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(f"Как будем гадать?", reply_markup=keyboard)

# разум, тело, душа 3
@dp.message(F.text.lower() == "разум, тело, душа")
async def tarot_camon_three_soul(message: types.Message):
    kb = [
        #[types.KeyboardButton(text="Добавить 2 карты")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass, deck_rand, deck_rand2 = three_cards('card_text_camon', 'soul')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_camon':
                    if podclass == 'soul':
                        if el == n[0]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваш разум</b>\n<b>{cards_up[0]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше тело</b>\n<b>{cards_up[1]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                        else:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваша душа</b>\n<b>{cards_up[2]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)
        
# состояние 3
@dp.message(F.text.lower() == "состояние")
async def tarot_camon_three_physic(message: types.Message):
    kb = [
        #[types.KeyboardButton(text="Добавить 2 карты")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass, deck_rand, deck_rand2 = three_cards('card_text_camon', 'physic')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_camon':
                    
                    if podclass == 'physic':
                        if el == n[0]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Физическое состояние</b>\n<b>{cards_up[0]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Физическое состояние\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Эмоциональное состояниео</b>\n<b>{cards_up[1]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML,
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Эмоциональное состояниео\n{cards_up[1]}: {res}\n")
                        else:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Душевное состояние</b>\n<b>{cards_up[2]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML,
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Душевное состояние\n{cards_up[2]}: {res}\n")
                    
            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard) 

# прошлое, настоящее, будущее 3
@dp.message(F.text.lower() == "прошлое, настоящее, будущее")
async def tarot_camon_three_past(message: types.Message):
    kb = [
        #[types.KeyboardButton(text="Добавить 2 карты")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass, deck_rand, deck_rand2 = three_cards('card_text_camon', 'past')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_camon':
                    if podclass == 'past':
                        if el == n[0]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше прошлое</b>\n<b>{cards_up[0]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML,
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше прошлое\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше настоящее</b>\n<b>{cards_up[1]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML,
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше настоящее\n{cards_up[1]}: {res}\n")
                        else:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше будущее</b>\n<b>{cards_up[2]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML,
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше будущее\n{cards_up[2]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard) 

# мысли и чувства 3
@dp.message(F.text.lower() == "мысли и чувства")
async def tarot_camon_three_think(message: types.Message):
    kb = [
        #[types.KeyboardButton(text="Добавить 2 карты")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass, deck_rand, deck_rand2 = three_cards('card_text_camon', 'think')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_camon':
                    if podclass == 'think':
                        if el == n[0]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Что вы думаете</b>\n<b>{cards_up[0]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML,
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Что вы думаете\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Что вы чувствуете</b>\n<b>{cards_up[1]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML,
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Что вы чувствуете\n{cards_up[1]}: {res}\n")
                        else:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Что вам нужно делать</b>\n<b>{cards_up[2]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML,
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Что вам нужно делать\n{cards_up[2]}: {res}\n")
                
            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)
    
# обычные значения 5
@dp.message(F.text.lower() == "обычный 5 карт")
async def tarot_camon_five(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Разум, тело, душа (5)")],
        [types.KeyboardButton(text="Состояние (5)")],
        [types.KeyboardButton(text="Прошлое, настоящее, будущее (5)")],
        [types.KeyboardButton(text="Мысли и чувства (5)")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(f"Как будем гадать?", reply_markup=keyboard)

# разум, тело, душа 5
@dp.message(F.text.lower() == "разум, тело, душа (5)")
async def tarot_camon_five_soul(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass = five_cards('card_text_camon', 'soul')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_camon':
                    if podclass == 'soul':
                        if el == n[0]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваш разум</b>\n<b>{cards_up[0]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше тело</b>\n<b>{cards_up[1]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                        elif el == n[2]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваша душа</b>\n<b>{cards_up[2]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")
                        elif el == n[3]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше прошлое</b>\n<b>{cards_up[3]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                        else:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше будущее</b>\n<b>{cards_up[4]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше будущее\n{cards_up[4]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)
          
# состояние 5
@dp.message(F.text.lower() == "состояние (5)")
async def tarot_camon_five_physic(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass = five_cards('card_text_camon', 'physic')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_camon':
                    
                    if podclass == 'physic':
                        if el == n[0]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Физическое состояние</b>\n<b>{cards_up[0]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Физическое состояние\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Эмоциональное состояниео</b>\n<b>{cards_up[1]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Эмоциональное состояниео\n{cards_up[1]}: {res}\n")
                        elif el == n[2]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Душевное состояние</b>\n<b>{cards_up[2]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Душевное состояние\n{cards_up[2]}: {res}\n")
                        elif el == n[3]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше прошлое</b>\n<b>{cards_up[3]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                        else:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше будущее</b>\n<b>{cards_up[4]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше будущее\n{cards_up[4]}: {res}\n")
                    
            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard) 

# прошлое, настоящее, будущее 5
@dp.message(F.text.lower() == "прошлое, настоящее, будущее (5)")
async def tarot_camon_five_past(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass = five_cards('card_text_camon', 'past')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_camon':
                    if podclass == 'past':
                        if el == n[0]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше прошлое</b>\n<b>{cards_up[0]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше прошлое\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше настоящее</b>\n<b>{cards_up[1]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше настоящее\n{cards_up[1]}: {res}\n")
                        elif el == n[2]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше будущее</b>\n<b>{cards_up[2]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше будущее\n{cards_up[2]}: {res}\n")
                        elif el == n[3]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Далекое прошлое</b>\n<b>{cards_up[3]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Далекое прошлое\n{cards_up[3]}: {res}\n")
                        else:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Далекое будущее</b>\n<b>{cards_up[4]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Далекое будущее\n{cards_up[4]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard) 

# мысли и чувства 5
@dp.message(F.text.lower() == "мысли и чувства")
async def tarot_camon_five_think(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass = five_cards('card_text_camon', 'think')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_camon':
                    if podclass == 'think':
                        if el == n[0]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Что вы думаете</b>\n<b>{cards_up[0]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Что вы думаете\n{cards_up[0]}: {res}\n")
                        elif el == n[1]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Что вы чувствуете</b>\n<b>{cards_up[1]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Что вы чувствуете\n{cards_up[1]}: {res}\n")
                        elif el == n[2]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Что вам нужно делать</b>\n<b>{cards_up[2]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Что вам нужно делать\n{cards_up[2]}: {res}\n")
                        elif el == n[3]:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше прошлое</b>\n<b>{cards_up[3]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                        else:
                            s = "img/"+str(el)+".jpeg"
                            image_from_pc = FSInputFile(s)
                            result = await message.answer_photo(
                                image_from_pc,
                                caption=f"<b>Ваше будущее</b>\n<b>{cards_up[4]}</b>: {res}\n",
                                parse_mode=ParseMode.HTML, 
                            )
                            file_ids.append(result.photo[-1].file_id)
                            #await message.answer(f"Ваше будущее\n{cards_up[4]}: {res}\n")
                
            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard) 
    
# 8 карт
@dp.message(F.text.lower() == "обычный 8 карт")
async def tarot_camon_nine(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n = eight_cards()
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT card_text_camon FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if el == n[0]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Сильные стороны человека</b>\n<b>{cards_up[0]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Сильные стороны человека\n{cards_up[0]}: {res}\n")
                elif el == n[1]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Слабые стороны человека</b>\n<b>{cards_up[1]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Слабые стороны человека\n{cards_up[1]}: {res}\n")
                elif el == n[2]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Что человек тщательно старается скрыть от остальных</b>\n<b>{cards_up[2]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Что человек тщательно старается скрыть от остальных\n{cards_up[2]}: {res}\n")
                elif el == n[3]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Что вызывает у человека крайне негативные чувства, эмоции и мысли</b>\n<b>{cards_up[3]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Что вызывает у человека крайне негативные чувства, эмоции и мысли\n{cards_up[3]}: {res}\n")
                elif el == n[4]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Что может человека радует и дарит позитивный настрой</b>\n<b>{cards_up[4]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Что может человека радует и дарит позитивный настрой\n{cards_up[4]}: {res}\n")
                elif el == n[5]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Чувства и эмоции по отношению к вам</b>\n<b>{cards_up[5]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Чувства и эмоции по отношению к вам\n{cards_up[5]}: {res}\n")
                elif el == n[6]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Что человеку нравится в вас, что привлекает</b>\n<b>{cards_up[6]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Что человеку нравится в вас, что привлекает\n{cards_up[6]}: {res}\n")
                elif el == n[7]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Что его отталкивает, абсолютно точно не нравится в вас</b>\n<b>{cards_up[7]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Что его отталкивает, абсолютно точно не нравится в вас\n{cards_up[7]}: {res}\n")
                

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)
        
# любовь и отношения
@dp.message(F.text.lower() == "любовь и отношения")
async def tarot_three_plus(message: types.Message):
    kb = [
        [types.KeyboardButton(text="любовь и отношения 3 карты")],
        [types.KeyboardButton(text="любовь и отношения 5 карт")],
        [types.KeyboardButton(text="любовь и отношения 6 карт")],
        [types.KeyboardButton(text="любовь и отношения 7 карт")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("Выбтрите количество карт", reply_markup=keyboard)

# любовь и отношения 3
@dp.message(F.text.lower() == "любовь и отношения 3 карты")
async def tarot_camon_three_soul(message: types.Message):
    kb = [
        #[types.KeyboardButton(text="Добавить 2 карты")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass, deck_rand, deck_rand2 = three_cards('card_text_love', 'soul')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_love':
                    if el == n[0]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Вы</b>\n<b>{cards_up[0]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                    elif el == n[1]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Ваши отношения</b>\n<b>{cards_up[1]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                    else:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Ваш партнер</b>\n<b>{cards_up[2]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)
        
# любовь и отношения 5
@dp.message(F.text.lower() == "любовь и отношения 5 карт")
async def tarot_camon_five_soul(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass = five_cards('card_text_love', 'soul')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_love':
                    if el == n[0]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Вы</b>\n<b>{cards_up[0]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                    elif el == n[1]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Ваши отношения</b>\n<b>{cards_up[1]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                    elif el == n[2]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Ваш партнер</b>\n<b>{cards_up[2]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")
                    elif el == n[3]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Ваше прошлое</b>\n<b>{cards_up[3]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                    else:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Ваше будущее</b>\n<b>{cards_up[4]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше будущее\n{cards_up[4]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)

# любовь и отношения 6
@dp.message(F.text.lower() == "любовь и отношения 6 карт")
async def tarot_camon_five_soul(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n = six_cards()
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT card_text_love FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                
                if el == n[0]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Чего вы на самом деле хотите от отношений</b>\n<b>{cards_up[0]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                elif el == n[1]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Уроки, которые вы вынесли из прошлых связей</b>\n<b>{cards_up[1]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                elif el == n[2]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Проблемы, которые мешают вам открыться противоположному полу</b>\n<b>{cards_up[2]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")
                elif el == n[3]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Готово ли ваше сердце к новым отношениям</b>\n<b>{cards_up[3]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                elif el == n[4]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Готов ли ваш разум к новому роману</b>\n<b>{cards_up[4]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                else:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Готовы ли вы к новым отношениям</b>\n<b>{cards_up[5]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше будущее\n{cards_up[4]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)
  
# любовь и отношения 7
@dp.message(F.text.lower() == "любовь и отношения 7 карт")
async def tarot_camon_five_soul(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n = seven_cards()
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT card_text_love FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                
                if el == n[0]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Настоящие причины проблем между партнерами</b>\n<b>{cards_up[0]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                elif el == n[1]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Поверхностные причины конфликтов, на которые тоже стоит обратить внимание</b>\n<b>{cards_up[1]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                elif el == n[2]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Ваши отношения с партнером в данный момент</b>\n<b>{cards_up[2]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")
                elif el == n[3]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Что вас ждет в ближайшем будущем</b>\n<b>{cards_up[3]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                elif el == n[4]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Что необходимо сделать, чтобы улучшить отношения</b>\n<b>{cards_up[4]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")
                elif el == n[5]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Действия (ваши или партнера), которые негативно влияют на вашу связь</b>\n<b>{cards_up[5]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                else:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Есть ли у вас шанс спасти отношения и укрепить связь</b>\n<b>{cards_up[6]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше будущее\n{cards_up[4]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)
    
# ситуация и вопрос
@dp.message(F.text.lower() == "ситуация и вопрос")
async def tarot_three_plus(message: types.Message):
    kb = [
        [types.KeyboardButton(text="ситуация и вопрос 3 карты")],
        [types.KeyboardButton(text="ситуация и вопрос 5 карт")],
        [types.KeyboardButton(text="ситуация и вопрос 10 карт")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("Выбтрите количество карт", reply_markup=keyboard)

# ситуация и вопрос 3
@dp.message(F.text.lower() == "ситуация и вопрос 3 карты")
async def tarot_camon_three_soul(message: types.Message):
    kb = [
        #[types.KeyboardButton(text="Добавить 2 карты")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass, deck_rand, deck_rand2 = three_cards('card_text_quest', 'soul')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_quest':
                    if el == n[0]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Ситцация</b>\n<b>{cards_up[0]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                    elif el == n[1]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Действие</b>\n<b>{cards_up[1]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                    else:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Исход</b>\n<b>{cards_up[2]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)
        
# ситуация и вопрос 5
@dp.message(F.text.lower() == "ситуация и вопрос 5 карт")
async def tarot_camon_five_soul(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass = five_cards('card_text_quest', 'soul')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_quest':
                    if el == n[0]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Ситуация</b>\n<b>{cards_up[0]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                    elif el == n[1]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Действие</b>\n<b>{cards_up[1]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                    elif el == n[2]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Исход</b>\n<b>{cards_up[2]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")
                    elif el == n[3]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Прошлое</b>\n<b>{cards_up[3]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                    else:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Будущее</b>\n<b>{cards_up[4]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше будущее\n{cards_up[4]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)

# ситуация и вопрос 10
@dp.message(F.text.lower() == "ситуация и вопрос 10 карт")
async def tarot_camon_five_soul(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n = ten_cards()
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT card_text_quest FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                
                if el == n[0]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Актуальные обстоятельства данного вопроса</b>\n<b>{cards_up[0]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                elif el == n[1]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Содействующая сила, либо препятствия</b>\n<b>{cards_up[1]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                elif el == n[2]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Прошлый опыт в решении поставленного вопроса</b>\n<b>{cards_up[2]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")
                elif el == n[3]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Недавнее прошлое</b>\n<b>{cards_up[3]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                elif el == n[4]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Возможное будущее за оговоренный при постановке вопроса период</b>\n<b>{cards_up[4]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                elif el == n[5]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Ближайшее будущее</b>\n<b>{cards_up[5]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                elif el == n[6]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Отношение к ситуации и то, каким он себя при этом ощущает</b>\n<b>{cards_up[6]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                elif el == n[7]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Окружение или другая точка зрения</b>\n<b>{cards_up[7]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                elif el == n[8]:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Надежды и опасения</b>\n<b>{cards_up[8]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                else:
                    s = "img/"+str(el)+".jpeg"
                    image_from_pc = FSInputFile(s)
                    result = await message.answer_photo(
                        image_from_pc,
                        caption=f"<b>Конечный исход ситуации</b>\n<b>{cards_up[9]}</b>: {res}\n",
                        parse_mode=ParseMode.HTML, 
                    )
                    file_ids.append(result.photo[-1].file_id)
                    #await message.answer(f"Ваше будущее\n{cards_up[4]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)
  
# работа и финансы
@dp.message(F.text.lower() == "работа и финансы")
async def tarot_three_plus(message: types.Message):
    kb = [
        [types.KeyboardButton(text="работа и финансы 3 карты")],
        [types.KeyboardButton(text="работа и финансы 5 карт")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("Выбтрите количество карт", reply_markup=keyboard)

# работа и финансы 3
@dp.message(F.text.lower() == "работа и финансы 3 карты")
async def tarot_camon_three_soul(message: types.Message):
    kb = [
        #[types.KeyboardButton(text="Добавить 2 карты")],
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass, deck_rand, deck_rand2 = three_cards('card_text_work', 'soul')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_work':
                    if el == n[0]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Текущая ситуация</b>\n<b>{cards_up[0]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                    elif el == n[1]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Решение</b>\n<b>{cards_up[1]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                    else:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Результат</b>\n<b>{cards_up[2]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)
        
# работа и финансы 5
@dp.message(F.text.lower() == "работа и финансы 5 карт")
async def tarot_camon_five_soul(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Вернуться")]
    ]
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    cards_up, n, category, podclass = five_cards('card_text_work', 'soul')
    try:
        connection = connToDb()
        connection.autocommit = True

        with connection.cursor() as cursor:
            for el in n:
                cursor.execute(
                        f"SELECT {category} FROM tarot_cards WHERE id = %s", (el+1,)
                    )
                res = cursor.fetchall()[0][0]
                if category == 'card_text_work':
                    if el == n[0]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Текущая ситуация</b>\n<b>{cards_up[0]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваш разум\n{cards_up[0]}: {res}\n")
                    elif el == n[1]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Решение</b>\n<b>{cards_up[1]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше тело\n{cards_up[1]}: {res}\n")
                    elif el == n[2]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Результат</b>\n<b>{cards_up[2]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваша душа\n{cards_up[2]}: {res}\n")
                    elif el == n[3]:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Прошлое</b>\n<b>{cards_up[3]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше прошлое\n{cards_up[3]}: {res}\n")
                    else:
                        s = "img/"+str(el)+".jpeg"
                        image_from_pc = FSInputFile(s)
                        result = await message.answer_photo(
                            image_from_pc,
                            caption=f"<b>Будущее</b>\n<b>{cards_up[4]}</b>: {res}\n",
                            parse_mode=ParseMode.HTML, 
                        )
                        file_ids.append(result.photo[-1].file_id)
                        #await message.answer(f"Ваше будущее\n{cards_up[4]}: {res}\n")

            print(f"[INFO] Complied")

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)
    else:
        if connection:
            connection.close()
            print("[INFO] PosgreSQL connection closed")
    await message.answer(f"Что дальше?", reply_markup=keyboard)

# матрица судьбы
@dp.message()
async def process_birthdate(message: types.Message):
    birthdate = message.text  # Получаем введённую дату
    # Здесь вы можете использовать переменную birthdate
    #await message.reply(f"Вы ввели дату рождения: {birthdate}")
    if last_user_msg:
        try:
            n = fate_matrix(birthday=birthdate)
            kb = [
            [types.KeyboardButton(text="Вернуться")]
            ]
            
            keyboard = types.ReplyKeyboardMarkup(
                keyboard=kb,
                resize_keyboard=True
            )
            image_from_pc = FSInputFile("matrix.png")
            await message.answer_photo(
                image_from_pc,
                caption=f"<b>Числа по большой окружности</b> - возраст\n<b>Цифры внутри кругов</b> - порядок расшифровки\n<b>Центр</b> - основное направление жизни, основные задачи, жизненный путь, внутренние качества",
                parse_mode=ParseMode.HTML, 
            )
            
        except Exception as ex:
            await message.reply(f"Неверный ввод")
            print(ex)
        else:
            try:
                connection = connToDb()
                connection.autocommit = True

                with connection.cursor() as cursor:
                    count = 0
                    for el in n:
                        if el != 22:
                            cursor.execute(
                                    f"SELECT card_text_camon FROM tarot_cards WHERE id = %s", (el+1,)
                                )
                        else:
                            cursor.execute(
                                    f"SELECT card_text_camon FROM tarot_cards WHERE id = %s", (1,)
                                )
                        res = cursor.fetchall()[0][0]
                        if count == 0:
                            if el != 22:
                                s = "img/"+str(el)+".jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Положительная энергия таланта</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            else:
                                s = "img/0.jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Положительная энергия таланта</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            file_ids.append(result.photo[-1].file_id)
                        elif count == 1:
                            if el != 22:
                                s = "img/"+str(el)+".jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Положительная энергия таланта</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            else:
                                s = "img/0.jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Положительная энергия таланта</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            file_ids.append(result.photo[-1].file_id)
                        elif count == 2:
                            if el != 22:
                                s = "img/"+str(el)+".jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Задачи до 40 лет, финансы, здоровье</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            else:
                                s = "img/0.jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Задачи до 40 лет, финансы, здоровье</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            file_ids.append(result.photo[-1].file_id)
                        elif count == 3:
                            if el != 22:
                                s = "img/"+str(el)+".jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Главная задача души в нынешнем воплощении, источник основных проблем</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            else:
                                s = "img/0.jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Главная задача души в нынешнем воплощении, источник основных проблем</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            file_ids.append(result.photo[-1].file_id)
                        elif count == 4:
                            if el != 22:
                                s = "img/"+str(el)+".jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Основное направление жизни, основные задачи, жизненный путь, внутренние качества</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            else:
                                s = "img/0.jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Основное направление жизни, основные задачи, жизненный путь, внутренние качества</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            file_ids.append(result.photo[-1].file_id)
                        elif count == 5:
                            if el != 22:
                                s = "img/"+str(el)+".jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Линия мужского рода - активные, динамичные качества</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            else:
                                s = "img/0.jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Линия мужского рода - активные, динамичные качества</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            file_ids.append(result.photo[-1].file_id)
                        elif count == 6:
                            if el != 22:
                                s = "img/"+str(el)+".jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Линия мужского рода - активные, динамичные качества</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            else:
                                s = "img/0.jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Линия мужского рода - активные, динамичные качества</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            file_ids.append(result.photo[-1].file_id)
                        elif count == 7:
                            if el != 22:
                                s = "img/"+str(el)+".jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Линия женского рода - пасивные, интуитивные качества</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            else:
                                s = "img/0.jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Линия женского рода - пасивные, интуитивные качества</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            file_ids.append(result.photo[-1].file_id)
                        elif count == 8:
                            if el != 22:
                                s = "img/"+str(el)+".jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Линия женского рода - пасивные, интуитивные качества</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            else:
                                s = "img/0.jpeg"
                                image_from_pc = FSInputFile(s)
                                result = await message.answer_photo(
                                    image_from_pc,
                                    caption=f"<b>{el}</b>\n<b>Линия женского рода - пасивные, интуитивные качества</b>\n{res}\n",
                                    parse_mode=ParseMode.HTML, 
                                )
                            file_ids.append(result.photo[-1].file_id)
                        count += 1

                    print(f"[INFO] Complied")

            except Exception as ex:
                print("[INFO] Error while working with PostgreSQL", ex)
            else:
                if connection:
                    connection.close()
                    print("[INFO] PosgreSQL connection closed")
            await message.answer(f"Что дальше?", reply_markup=keyboard)
    if not last_user_msg:
        await message.answer(f"Выберите команду из предложенных")
    

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
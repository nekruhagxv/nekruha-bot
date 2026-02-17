import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = '8145143763:AAHMv-HBl5rZmHzHd36741g9FTI1dwp_BhI'
ADMIN_ID = 1041362953 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="🚗 VW Polo"), types.KeyboardButton(text="🏎️ Toyota Camry"))
    builder.row(types.KeyboardButton(text="🇩🇪 BMW"), types.KeyboardButton(text="🏙️ Mercedes"))
    builder.row(types.KeyboardButton(text="🇯🇵 Nissan"), types.KeyboardButton(text="💎 Lexus"))
    builder.row(types.KeyboardButton(text="🇺🇸 Chevrolet"), types.KeyboardButton(text="🇰🇷 Hyundai"))
    builder.row(types.KeyboardButton(text="🛞 Диски (Street)"), types.KeyboardButton(text="🎨 Наклейки"))
    builder.row(types.KeyboardButton(text="🎨 Пленка"), types.KeyboardButton(text="🎺 Выхлопные системы"))
    builder.row(types.KeyboardButton(text="⚙️ Тех запчасти"), types.KeyboardButton(text="👨‍💻 Связь с админом"))
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\nВыбери свой автомобиль или раздел тюнинга:",
        reply_markup=main_menu()
    )

@dp.message(F.text.in_([
    "🚗 VW Polo", "🏎️ Toyota Camry", "🇩🇪 BMW", "🏙️ Mercedes", 
    "🇯🇵 Nissan", "💎 Lexus", "🇺🇸 Chevrolet", "🇰🇷 Hyundai"
]))
async def car_tuning_handler(message: types.Message):
    text = (
        f"🛠 **Тюнинг-пакет для {message.text}**\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "⚪️ **Clear Tail (Прозрачная задняя оптика):**\n"
        "└ от 160 000 ₸ | 32 000 ₽\n\n"
        "✅ **Stage 1 (Чип-тюнинг):**\n"
        "└ от 65 000 ₸ | 13 000 ₽\n\n"
        "✅ **Street Setup (Занижение):**\n"
        "└ от 90 000 ₸ | 18 000 ₽\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "💬 *Для заказа пишите админу.*"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "🛞 Диски (Street)")
async def wheels_menu(message: types.Message):
    text = (
        "🛞 **Витрина дисков (Street Style)**\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "🇯🇵 JAPAN: Rays TE37, Work Meister, Enkei RPF1, SSR, BBS Japan\n\n"
        "🇩🇪 GERMANY: BBS RS, Borbet A, Rotiform, Keskin, OZ\n\n"
        "🇺🇸 USA: Vossen CV3, HRE, Forgiato, Adv.1, American Racing\n\n"
        "🇷🇺 RUSSIA: Slik (Ковка), ВСМПО, СКАД, K&K, Mag Custom\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "💰 **Комплект: от 280 000 ₸ | 56 000 ₽**"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "🎨 Наклейки")
async def stickers_menu(message: types.Message):
    text = (
        "🏷 **Доступные наклейки:**\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "🔹 513 | OGM | nekrovxg | 326power\n"
        "🔹 Тяжелый стрит | SWAG | TTblond\n"
        "🔹 FLOWA | RED BULL | STREETCARSPECIAL\n"
        "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        "💰 **Цена: от 2 500 ₸ | 500 ₽**"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "🎨 Пленка")
async def vinyl_menu(message: types.Message):
    text = "🎨 **Оклейка:**\n- Защита (PPF): от 750к ₸\n- Винил: от 500к ₸\n- Антихром: 45к ₸"
    await message.answer(text)

@dp.message(F.text == "🎺 Выхлопные системы")
async def exhaust_menu(message: types.Message):
    text = (
        "🎺 **Выхлопные системы:**\n"
        "└ Remus: от 450 000 ₸\n"
        "└ Magnaflow: от 380 000 ₸\n"
        "└ 326 Power: от 550 000 ₸"
    )
    await message.answer(text)

@dp.message(F.text == "⚙️ Тех запчасти")
async def spare_parts(message: types.Message):
    await message.answer("⚙️ **Запчасти:**\nПришлите VIN-код в чат для подбора.")

@dp.message(F.text == "👨‍💻 Связь с админом")
async def contact_admin(message: types.Message):
    await message.answer("По всем вопросам пишите напрямую или отправьте сообщение здесь.")

@dp.message()
async def admin_forward(message: types.Message):
    if message.chat.id != ADMIN_ID:
        await bot.send_message(ADMIN_ID, f"📩 **Сообщение от @{message.from_user.username}:**\n{message.text}")
        await message.answer("Сообщение доставлено админу!")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
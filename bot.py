import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton



API_TOKEN = "8756157675:AAHO6Nk1hJUtNvs_y3-LF9EgFjhjmlnSK34"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message_handler(CommandStart())
async def start(message: Message):
    await message.answer("Привіт я твій телеграм бот. Напиши /help або /about.")

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Ось, що я вмію:\n/start - привітання\n/help - довідка\n/about")

@dp.message(Command("about"))
async def about_command(message: Message):
    await message.answer("я створений на Python з бібліотекою Aiogram!")


@dp.message(Command("menu"))
async def show_menu(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text ="Привіт"), KeyboardButton(text = "Як справи?")],

            [KeyboardButton(text = "Анекдот")]
    ],
        resize_keyboard=True
    )
    await message.answer("Вибери опцію:", reply_markup=keyboard)



@dp.message()
async def handle_message(message: Message):
    text = message.text
    if text == "Привіт":
        await message.answer("Привіт-привіт")
    elif text == "Як справи?":
        await message.answer("Усе чудово! А в тебе?")
    elif text == "Анекдот":
        await message.answer("Приходить вампір до вампірського нічного бару, підійшов до стійки біля бару.Бармен: - Що хочете випити: крові 1-ї, 2-ї, 3-ї групи, може крові тварини Вампір: - Налийте мені кип'яченої води. Усі у барі застигли. Бармен: — Ви захворіли чи вам погано? Вампір: - Та ні! Налийте мені кип'яченої води. У цей час дістає з кишені використану прокладку і каже: — Я сьогодні вирішив побалуватися чайком.")
    else:
        await message.answer("Натисни одну з кнопок")



async def main():
    print("Бот запущений...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
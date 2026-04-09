import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

import asyncio


API_TOKEN = "8756157675:AAHO6Nk1hJUtNvs_y3-LF9EgFjhjmlnSK34"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привіт! я телеграм бот. напиши команду /help, щоб дізнатися, що я вмію!")



@dp.message(Command("help"))
async def help_command(message: Message):
    help_text = (
        "Доступні команди:\n"
        "/start - Привітатися з ботом\n"
        "/help - Показати цю довідку\n\n"
        "Я поки буду для тебе не настільки корисним, але може в майбутньому я стану розумніше"
    )
    await message.answer(help_text)


async def main():
    print("Бот запущений...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# Сюди вставляємо свій токен з BotFather
API_TOKEN = "8756157675:AAHO6Nk1hJUtNvs_y3-LF9EgFjhjmlnSK34"

# Створюємо бота і диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обробник команди /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт! Я твій перший бот!")

@dp.message(Сommand("start"))
async def start_command(message: Message):
    await message.answer("Привіт! я телеграм бот. напиши команду /help, щоб дізнатися, що я вмію!")

@dp.message(Сommand("help"))
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
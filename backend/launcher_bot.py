import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup

TELEGRAM_TOKEN = '7742278507:AAG5cqgdDt3caIUlY9a-6wqZQ3WmNzi809A'
WEBAPP_URL = 'https://miniapp.217.114.2.15'  # URL вашего развернутого frontend приложения

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Открыть чат поддержки",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )]
        ]
    )
    
    await message.answer(
        "Привет! Нажмите на кнопку ниже, чтобы открыть чат поддержки:",
        reply_markup=keyboard
    )

@dp.message()
async def echo(message: types.Message):
    await message.answer("Используйте /start для получения доступа к чату поддержки")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

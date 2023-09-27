import asyncio
from aiogram import types
from aiogram import Bot, Dispatcher
from aiogram.types import Message as Ms
from handlers import router
from aiogram.filters.command import Command
from aiogram import F

TOKEN_API = '6412544139:AAEs_OJXnWcML3gVMjlQ7wX2aIs9MvmzTZ8'
bot = Bot(token=TOKEN_API)
dp = Dispatcher()
dp.include_router(router)


@dp.message(Command('start'))
async def send_greeting(message: Ms):
    await message.answer('Привет! Давай найдем твой заказ.')






async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
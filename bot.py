from keep_alive import keep_alivefrom aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

TOKEN = "8903550566:AAFFjzsFE8oh1AO_AHXpiLnb1ArCk7PoeTI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("🔥 GBX Coupon Bot Online Hai")

async def main():
    await dp.start_polling(bot)

keep_alive()
asyncio.run(main())

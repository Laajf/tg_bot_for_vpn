from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice, PreCheckoutQuery ,InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from utils.create_and_get_config import create_and_get_config
from aiogram.types.input_file import FSInputFile
from aiogram import types
from aiogram.filters import Command
from aiogram import Router

BOT_TOKEN = "7706530077:AAHbhHTE9VvPZaTAnTDRRrDj1EFTx6JnMog"
PAYMENT_PROVIDER_TOKEN = "1744374395:TEST:ff512475568d60d16e73"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    print(1111)
    await message.answer("Привет! Я бот для покупки red_panda_vpn.Используй /help чтобы узнать больше о боте.")
    print("11111")


@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer("""Список команд бота:
    1./buy_1 - купить впн на 1 месяц
    2./buy_2 - купить впн на 2 месяца
    3./buy_3 - купить впн на 3 месяца
    """)

@dp.message(Command("buy_1"))
async def buy_process(message: types.Message):
    try:

        prices = [LabeledPrice(label="Товар", amount=5000)]
        await bot.send_invoice(
            chat_id=message.chat.id,
            title="Впн",
            description="Псоле оплаты вам будет выдан конфиг впн",
            provider_token=PAYMENT_PROVIDER_TOKEN,
            currency="RUB",
            prices=prices,
            start_parameter="unique_start_parameter",
            payload="vpn_1_month"
        )
    except Exception as e:
        await message.answer(f"Произошла ошибка при создании счета: {str(e)}")

@dp.message(Command("buy_2"))
async def buy_process(message: types.Message):
    try:

        prices = [LabeledPrice(label="Товар", amount=10000)]
        await bot.send_invoice(
            chat_id=message.chat.id,
            title="Тестовый товар",
            description="Описание тестового товара",
            provider_token=PAYMENT_PROVIDER_TOKEN,
            currency="RUB",
            prices=prices,
            start_parameter="unique_start_parameter",
            payload="vpn_2_month"
        )
    except Exception as e:
        await message.answer(f"Произошла ошибка при создании счета: {str(e)}")

@dp.message(Command("buy_3"))
async def buy_process(message: types.Message):
    try:

        prices = [LabeledPrice(label="Товар", amount=15000)]
        await bot.send_invoice(
            chat_id=message.chat.id,
            title="Тестовый товар",
            description="Описание тестового товара",
            provider_token=PAYMENT_PROVIDER_TOKEN,
            currency="RUB",
            prices=prices,
            start_parameter="unique_start_parameter",
            payload="vpn_3_month"
        )
    except Exception as e:
        await message.answer(f"Произошла ошибка при создании счета: {str(e)}")


@dp.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    try:
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    except Exception as e:
        print(f"Ошибка при обработке предварительного запроса: {str(e)}")


@dp.message(lambda message: message.content_type == types.ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    payload = message.successful_payment.invoice_payload
    await message.answer(payload)
    if payload == "vpn_1_month":
        await message.answer("Спасибо за покупку! Сейчас вам будет выдан конфиг  VPN на 1 месяц.")

        msg = await message.answer("Процесс выдачи конфига VPN начинается.")


        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. ")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. .")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. . .")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. ")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. .")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. . .")


        config_file_path = create_and_get_config(
            1) + ".sswan"
        config_file = FSInputFile(config_file_path)
        await bot.send_document(message.chat.id, config_file)

        await asyncio.sleep(1)
        await msg.edit_text("Процесс завершен.")






    elif payload == "vpn_2_month":
        await message.answer("Спасибо за покупку! Сейчас вам будет выдан конфиг  VPN на 2 месяца.")

        msg = await message.answer("Процесс выдачи конфига VPN начинается.")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. ")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. .")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. . .")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. ")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. .")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. . .")


        config_file_path = create_and_get_config(
            2) + ".sswan"
        config_file = FSInputFile(config_file_path)
        await bot.send_document(message.chat.id, config_file)

        await asyncio.sleep(1)
        await msg.edit_text("Процесс завершен.")

    elif payload == "vpn_3_month":
        await message.answer("Спасибо за покупку! Сейчас вам будет выдан конфиг  VPN на 3 месяца.")

        msg = await message.answer("Процесс выдачи конфига VPN начинается.")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. ")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. .")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. . .")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. ")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. .")

        await asyncio.sleep(1)
        await msg.edit_text("Процесс идет. . .")


        config_file_path = create_and_get_config(
        3) + ".sswan"
        config_file = FSInputFile(config_file_path)
        await bot.send_document(message.chat.id, config_file)

        await asyncio.sleep(1)
        await msg.edit_text("Процесс завершен.")

    else:
        await message.answer("Спасибо за покупку!")


async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка при запуске бота: {str(e)}")

if __name__ == '__main__':
    asyncio.run(main())

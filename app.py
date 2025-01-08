from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice, PreCheckoutQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.input_file import FSInputFile
import asyncio
from utils.create_and_get_config import create_and_get_config
from aiogram.filters import Command
from aiogram import Router
from repository.chek_free import examination, add_record

BOT_TOKEN = "7706530077:AAHbhHTE9VvPZaTAnTDRRrDj1EFTx6JnMog"
PAYMENT_PROVIDER_TOKEN = "1744374395:TEST:ff512475568d60d16e73"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Купить VPN на 1 месяц", callback_data="buy_1")],
        [InlineKeyboardButton(text="Купить VPN на 2 месяца", callback_data="buy_2")],
        [InlineKeyboardButton(text="Купить VPN на 3 месяца", callback_data="buy_3")],
        [InlineKeyboardButton(text="Получить бесплатный VPN", callback_data="free_vpn")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")]
    ])

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "\U0001F60E Привет! Я бот для покупки VPN. Выберите опцию из меню ниже.",
        reply_markup=get_main_keyboard()
    )

@dp.callback_query()
async def handle_callback(query: types.CallbackQuery):
    if query.data == "help":
        await query.message.edit_text(
            "\U0001F4AC **Информация:**\n\n"
            "1. **Безопасность платежей:** Платежи через Telegram безопасны. Мы не получаем ваших данных о карте, все операции проходят через зашифрованное соединение Telegram.\n\n"
            "2. **Что такое VPN:** VPN (Virtual Private Network) — это технология, которая защищает ваши данные в интернете и обходит ограничения на доступ к сайтам. "
            "Наша технология обеспечивает стабильное соединение и максимальную конфиденциальность.\n\n"
            "3. **Как установить VPN?**\n"
            "   - Инструкции для iOS, macOS, Windows, Linux и Android можно найти в [руководстве по настройке IKEv2 VPN](https://github.com/hwdsl2/setup-ipsec-vpn/blob/master/docs/ikev2-howto.md#os-x-macos).\n\n"
            "4. **Часто задаваемые вопросы:**\n"
            "   - **Как я получу доступ к VPN?** После оплаты вы получите конфигурационный файл.\n"
            "   - **Подходит ли VPN для мобильных устройств?** Да, вы можете использовать его на телефоне, планшете и компьютере.",
            reply_markup=get_main_keyboard()
        )

    elif query.data.startswith("buy_"):
        duration = query.data.split("_")[1]
        await process_purchase(query.message, int(duration))
    elif query.data == "free_vpn":
        if examination(query.from_user.id):
            await query.message.answer("Вы уже использовали бесплатный впн")
        else:
            add_record(query.from_user.id)
            await query.message.answer("Вы еще не использовали бесплатный впн")


async def process_purchase(message: types.Message, duration: int):
    amounts = {1: 5000, 2: 10000, 3: 15000}
    prices = [LabeledPrice(label=f"VPN на {duration} месяц(а)", amount=amounts[duration])]
    try:
        await bot.send_invoice(
            chat_id=message.chat.id,
            title=f"VPN на {duration} месяц(а)",
            description="После оплаты вы получите конфигурацию для VPN.",
            provider_token=PAYMENT_PROVIDER_TOKEN,
            currency="RUB",
            prices=prices,
            start_parameter="unique_start_parameter",
            payload=f"vpn_{duration}_month"
        )
    except Exception as e:
        await message.answer(f"\u26A0 Ошибка при создании счета: {str(e)}")

@dp.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    try:
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    except Exception as e:
        print(f"Ошибка при обработке предварительного запроса: {str(e)}")

@dp.message(lambda message: message.successful_payment)
async def process_successful_payment(message: types.Message):
    payload = message.successful_payment.invoice_payload
    duration = payload.split("_")[1]
    await message.answer(f"\U0001F389 Спасибо за покупку VPN на {duration} месяц(а)!\n\U0001F4BE Ваш файл сейчас будет отправлен.")

    config_file_path = create_and_get_config(int(duration)) + ".sswan"
    config_file = FSInputFile(config_file_path)
    await bot.send_document(message.chat.id, config_file)

    await message.answer("\U0001F512 Конфигурация отправлена! Приятного пользования.")

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка при запуске бота: {str(e)}")

if __name__ == '__main__':
    asyncio.run(main())

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice, PreCheckoutQuery
import asyncio
from utils.create_and_get_config import create_and_get_config
from aiogram.filters import Command
from aiogram import Router
from repository.chek_free import examination, add_record
from payment1 import payment1
from check_payment import check_payment

BOT_TOKEN = "7706530077:AAHbhHTE9VvPZaTAnTDRRrDj1EFTx6JnMog"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

def get_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Купить VPN на 1 месяц", callback_data="buy_1")],
        [InlineKeyboardButton(text="Получить бесплатный VPN", callback_data="free_vpn")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")]
    ])

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "\U0001F60E Привет! Я бот для выдачи VPN. Выберите опцию из меню ниже.",
        reply_markup=get_main_keyboard()
    )

@dp.callback_query()
async def handle_callback(query: types.CallbackQuery):
    if query.data == "help":
        await query.message.edit_text(
            "\U0001F4AC **Информация:**\n\n"
            "1. **Что такое VPN:** VPN (Virtual Private Network) — это технология, которая защищает ваши данные в интернете и обходит ограничения на доступ к сайтам.\n\n"
            "2. **Как установить VPN?**\n"
            "   - Инструкции для iOS, macOS, Windows, Linux и Android можно найти в [руководстве по настройке IKEv2 VPN](https://github.com/hwdsl2/setup-ipsec-vpn/blob/master/docs/ikev2-howto.md#os-x-macos).\n\n"
            "3. **Часто задаваемые вопросы:**\n"
            "   - **Как я получу доступ к VPN?** После оплаты или запроса бесплатной версии бот выдаст конфигурационный файл.\n"
            "   - **Подходит ли VPN для мобильных устройств?** Да, вы можете использовать его на телефоне, планшете и компьютере.",
            reply_markup=get_main_keyboard()
        )

    elif query.data == "buy_1":
        await process_purchase(query.message)

    elif query.data == "free_vpn":
        if examination(query.from_user.id):
            await query.message.answer("Вы уже использовали бесплатный VPN.")
        else:
            add_record(query.from_user.id)
            config_file_path = create_and_get_config(1) + ".sswan"
            await query.message.answer_document(types.FSInputFile(config_file_path), caption="Ваш VPN конфиг.")
            await query.message.answer("\U0001F512 Конфигурация отправлена! Приятного пользования.")

async def process_purchase(message: types.Message):
    user_id = message.from_user.id
    link, label = payment1(user_id)
    await message.answer("Ваша ссылка для оплаты: \n" + link)
    payment_status = check_payment(label)  

    if payment_status == "success":
        await process_successful_payment(message)
    else:
        await message.answer("Оплата не прошла успешно. Пожалуйста, попробуйте снова.")

#@dp.pre_checkout_query()
#async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    #try:
        #await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    #except Exception as e:
        #print(f"Ошибка при обработке предварительного запроса: {str(e)}")

#@dp.message(lambda message: message.successful_payment)
async def process_successful_payment(message: types.Message):

    await message.answer("\U0001F389 Спасибо за покупку VPN на 1 месяц!\n\U0001F4BE Ваш файл сейчас будет отправлен.")
    
    config_file_path = create_and_get_config(1) + ".sswan"
    config_file = types.FSInputFile(config_file_path)
    await bot.send_document(message.chat.id, config_file)
    
    await message.answer("\U0001F512 Конфигурация отправлена! Приятного пользования.")

async def main():
    try:
        print("Online yomao")
        await dp.start_polling(bot)
        print("Bot online!")
    except Exception as e:
        print(f"Произошла ошибка при запуске бота: {str(e)}")

if __name__ == '__main__':
    asyncio.run(main())

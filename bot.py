import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
callback_data = "0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Дома", callback_data="1"),
            InlineKeyboardButton("На улице", callback_data="2"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Где вы хотите провести время?:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query.data == "1":
        keyboard = [
            [
                InlineKeyboardButton("Кино", callback_data="11"),
                InlineKeyboardButton("Настолки", callback_data="12"),
                InlineKeyboardButton("Творчество", callback_data="13"),
                InlineKeyboardButton("Рецепты", callback_data="14"),
                InlineKeyboardButton("Чтение", callback_data="15"),
            ]
        ]
    if query.data == "2":
        keyboard = [
            [
                InlineKeyboardButton("Игры", callback_data="21"),
                InlineKeyboardButton("Еда", callback_data="22"),
                InlineKeyboardButton("Места в Кзн", callback_data="23"),
                InlineKeyboardButton("Марш. л.", callback_data="24"),
                InlineKeyboardButton("Спорт", callback_data="25"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.answer()
        await query.edit_message_text(text=f"Выберите что вы хотите", reply_markup=reply_markup )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    application = Application.builder().token("7357029258:AAGxj-fiM3uwPuERpn0JoTNH-MS1pJWeMNo").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Token API yang didapat dari BotFather
TOKEN = '7370299001:AAGUnLINQ12RYpncFVcrVjDuS-FHb-zgsJk'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Halo! Saya adalah bot Anda. Bagaimana saya bisa membantu?')

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Perintah yang tersedia: /start, /help')

async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    await update.message.reply_text(f': {text}')

def main() -> None:
    # Inisialisasi Application dengan token
    application = Application.builder().token(TOKEN).build()

    # Daftarkan handler untuk perintah start dan help
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Mulai polling
    application.run_polling()

def echo(update, context):
    update.message.reply_text(update.message.text)

dp.add_handler(CommandHandler("echo", echo))


if __name__ == '__main__':
    main()

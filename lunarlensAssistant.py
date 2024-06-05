import pathlib
import textwrap
import os
import google.generativeai as genai
import tracemalloc
import nest_asyncio
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import google.ai.generativelanguage as glm
from dotenv import load_dotenv
from load_creds import load_creds, SCOPES
from IPython.display import display
from IPython.display import Markdown
import google_auth_oauthlib.flow


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

load_dotenv()

tracemalloc.start()
nest_asyncio.apply()

TOKEN: Final[str] = "7480253592:AAFFwrQ_IPLj1jbBoVssE2jnE9POUenrSNA"
BOT_USERNAME: Final[str] = "@lunarlensAssistant_bot"
GEMINI_API_KEY: Final[str] = os.getenv("AIzaSyD7rqwU-R7CjcHcJ8x_ihdh8q3aReUjskg")
creds = load_creds()
CLIENT_SECRETS_FILE="C:\Users\acerr\PycharmProjects\pythonProject\client_secret.json"

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(CLIENT_SECRETS_FILE,scopes=SCOPES)
flow.redirect_uri = 'https://web.telegram.org/a/#7480253592'

genai.configure(api_key=GEMINI_API_KEY)
genai.configure(credentials=creds)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
model = genai.GenerativeModel('gemini-1.5-flash')

generative_service_client = glm.GenerativeServiceClient()
retriever_service_client = glm.RetrieverServiceClient()
permission_service_client = glm.PermissionServiceClient()

print()
print('Available base models:', [m.name for m in genai.list_models()])

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Halo! Senang Bertemu denganmu. Nama Saya Lunar lens, Saya Asisten yang siap memandu perjalanan antariksamu :)')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Ya ada yang bisa saya bantu?')

def handle_response(text: str) -> str:
    text = text.lower()

    if "hi" in text or "hello" in text:
        return "Hai :) Ada yang bisa ku bantu ?"
    elif "Apa kabarmu ?" in text:
        return "Baik, bagaimana denganmu ?"
    elif "Siapa Namamu ?" in text:
        return "Saya Lunar Lens, sahabat yang menemani perjalanan antariksamu :)"
    elif "Terima Kasih" in text:
        return "Sama-sama, semoga kamu menikmati perjalanan antariksamu :)"
    elif "Selamat Tinggal" in text:
        return "Dada, sampai jumpa kembali"
    else:
        return "aku nggak ngerti kamu lagi ngetik apa :("

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response)

async def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Set up webhook URL dengan await
    await app.bot.set_webhook(f'https://t.me/lunarlensAssistant_bot')

    # Run webhook
    await app.run_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

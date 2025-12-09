from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import requests
import os

BOT_TOKEN = os.getenv("8213749728:AAF8LJJ11pVwpVCjTcbSU5UIZ2-3BF0C08s")

def terabox_direct(url):
    api = "https://api.teraboxlink.com/api?url=" + url
    resp = requests.get(api).json()
    if resp["status"] == "success":
        return resp["download_url"]
    return "❌ Direct link नहीं मिला"

async def start(update, context):
    await update.message.reply_text("Terabox Direct Link Bot Ready! लिंक भेजें!")

async def handle_message(update, context):
    url = update.message.text
    direct = terabox_direct(url)
    await update.message.reply_text(direct)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()

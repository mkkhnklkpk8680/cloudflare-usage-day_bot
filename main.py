from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def usage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات وصل شد ✅")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("usage", usage))

app.run_polling()

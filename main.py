from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("8964633650:AAGJGCC-ARRqqBMji5L8oQByqcrq2IRE_9M")

async def usage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات وصل شد ✅")

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("usage", usage))

app.run_polling()

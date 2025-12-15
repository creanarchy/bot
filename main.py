import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton("Взойти", url="https://t.me/creanarchycorp_bot/riseoflilboy")]]
    await update.message.reply_text(
        "Нажми кнопку, чтобы начать игру 🩸",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(os.getenv("BOT_TOKEN")).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "8699109262:AAFtEHxvpXYRikxPOzHCQKRRbzR01SEIRL0"

sfide = [
    "😈 SFIDA: manda un vocale sensuale",
    "🔥 SFIDA: tagga chi baceresti ora",
    "💋 SFIDA: descrivi il tuo tipo ideale",
    "👀 SFIDA: manda un emoji hot",
    "🎙️ SFIDA: fai un complimento provocante"
]
punti {}

async def start(update, context):
    await update.message.reply_text(
        "🎮 Benvenuto nel gioco delle sfide!\n\nUsa /sfida per giocare 😏\nUsa /punti per vedere i tuoi punti 🏆"
    )

async def sfida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    scelta = random.choice(sfide)
    await update.message.reply_text(scelta)

async def punti_cmd(update, context):
    await update.message.reply_text("TEST OK")
    

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("sfida", sfida))

app.add_handler(CommandHandler("punti", punti_cmd))

print("Bot avviato 😎")

app.run_polling()

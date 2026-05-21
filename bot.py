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

async def sfida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    scelta = random.choice(sfide)
    await update.message.reply_text(scelta)

async def punti_cmd(update, context):
    user_id = update.effective_user.id
    await update.message.reply_text(f"🏆 Hai {punti.get(user_id, 0)} punti")
    

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("sfida", sfida))

app.add_handler(CommandHandler("punti", punti_cmd))

print("Bot avviato 😎")

app.run_polling()

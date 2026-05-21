import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 🎲 SFIDE
sfide = [
    "Fai un complimento a qualcuno 😏",
    "Racconta una figuraccia 😂",
    "Manda la tua emoji del giorno 🔥",
    "Scrivi 'sono il re/la regina del gruppo 👑'",
    "Racconta un segreto innocente 👀"
]

# 🏆 PUNTI
punti = {}

def get_points(user_id):
    return punti.get(user_id, 0)

def add_points(user_id):
    punti[user_id] = get_points(user_id) + 1


# 🎮 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Benvenuto nel GAME delle SFIDE!\n\n"
        "👉 Usa /sfida per giocare\n"
        "👉 Usa /punti per vedere i punti"
    )


# 🎲 SFIDA
async def sfida(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    sfida = random.choice(sfide)

    add_points(user_id)

    await update.message.reply_text(
        f"🎲 SFIDA ATTIVA!\n\n{sfida}\n\n🏆 +1 punto!"
    )


# 🏆 PUNTI
async def punti_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(
        f"🏆 Hai {get_points(user_id)} punti"
    )


# 🚀 BOT SETUP
app = Application.builder().token("INSERISCI_TOKEN_QUI").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sfida", sfida))
app.add_handler(CommandHandler("punti", punti_cmd))

app.run_polling()

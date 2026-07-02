from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Il bot funziona 😄")


async def cucina(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍽️ *Ecco a te l'elenco delle ricette da noi possedute!*\n\n"
        "🥪 *Salato:*\n"
        "• Chips /chips\n"
        "• Hotdog /hotdog\n"
        "• Pasta /pasta\n"
        "• Hamburger /hamburger\n"
        "• Nachos /nachos\n"
        "• Wrap /wrap\n"
        "• Uramaki /uramaki\n"
        "• Sashimi /sashimi\n"
        "• Nigiri /nigiri\n"
        "• Hosomaki /hosomaki\n"
        "• Tacos /tacos\n\n"
        "🍰 *Dolci:*\n"
        "• Torta /torta\n"
        "• Macaron /macaron"
    )

    await update.message.reply_text(text, parse_mode="Markdown")


async def chips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍟 *Eccoti le chips:*\n\n"
        "Patata > Tagliere > Chips x4\n"
        "Chips > Friggitrice > Chips Cotte\n\n"
        "• Chips alla paprika:\n"
        "Chips Cotte + Paprika > Chips alla Paprika x2\n\n"
        "Da usare sul banco da lavoro."
    )

    await update.message.reply_text(text, parse_mode="Markdown")



    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cucina", cucina))
    app.add_handler(CommandHandler("chips", chips))

    
    app.run_polling()

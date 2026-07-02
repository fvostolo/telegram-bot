from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Il bot funziona 😄")


async def cucina(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍽️ *Ecco a te l'elenco delle nostre ricette!*\n\n"
        "🥪 *Salato:*\n\n"
        "» Chips /chips\n\n"
        "» Hotdog /hotdog\n\n"
        "» Pasta /pasta\n\n"
        "» Hamburger /hamburger\n\n"
        "» Nachos /nachos\n\n"
        "» Wrap /wrap\n\n"
        "» Uramaki /uramaki\n\n"
        "» Sashimi /sashimi\n\n"
        "» Nigiri /nigiri\n\n"
        "» Hosomaki /hosomaki\n\n"
        "» Tacos /tacos\n\n"
        "🍰 *Dolci:*\n\n"
        "» Torta /torta\n\n"
        "» Macaron /macaron"
    )

    await update.message.reply_text(text, parse_mode="Markdown")


async def chips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍟 *Eccoti le chips:*\n\n"
        "Patata x1> Tagliere > Chips x4\n"
        "Chips > Friggitrice > Chips Cotte\n\n"
        "» Chips alla paprika:\n"
        "Chips Cotte x1 + Paprika x1 > Chips alla Paprika x2\n\n"
        "Da usare sul banco da lavoro."
    )

    await update.message.reply_text(text, parse_mode="Markdown")


async def hotdog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌭 *Eccoti gli Hotdog:*\n\n"
        "» HotDog classico:\n"
        "x1 Pane per hotdog + x1 Wurstel cotto + x1 Maionese + x1 Ketchup › Banco da Lavoro\n\n"
        "» HotDog Vegano:\n"
        "x1 Pane per hotdog + x1 Wurstel veg cotto + x1 Lattuga + x1 Pomodoro › Banco da Lavoro > x4 Hot dog veg\n\n"
        "» HotDog con Cipolla Croccante:\n"
        "x1 Pane per hotdog + x1 Wurstel cotto + x1 Cipolle fritte + x1 Senape › Banco da lavoro > HotDog con Cipolla x4\n\n"
        "Il pane per hotdog si ottiene tagliando pane per hamburger su un tagliere con il coltello."
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def pasta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍝 *Ecco a te i vari tipi di pasta:\n\n"
        "» Cacio e Pepe:\n"
        "x2 Pecorino + x1 Pepe + x1 Spaghetti cotti › Padella  › x4 Spaghetti alla cacio e pepe\n\n"
        "» Caviale:\n"
        "x1 Pepe + x1 Caviale + x1 Spaghetti cotti  › Padella › x3 Pasta al caviale\n\n"
        "» Carbonara:\n"
        "x1 Pecorino + x1 Guanciale a dadini + x1 Tuorlo + x1 Spaghetti cotti › Padella > x4 Spaghetti alla carbonara\n\n"
        "» Amatriciana:\n"
        "x1 Sugo + x1 Pecorino + x1 Guanciale a dadini + x1 Spaghetti cotti › Padella > x4 Spaghetti all’amatriciana\n\n"
        "Spaghetti cotti: si ottengono cucinando la pasta in padella con un mestolo."
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def hamburger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍔 *Ecco a te i vari hamburger:\n\n"
        "» Cheeseburger:\n"
        "x1 Pane per hamburger + x1 Hamburger di manzo + x1 Cheddar + x1 Bacon + x1 Pane per hamburger › Banco da lavoro  › x5 Cheeseburger con bacon\n\n"
        "» Carne:\n"
        "x1 Pane per hamburger + x1 Fetta di pomodoro + x1 Hamburger di manzo + x1 Cheddar + x1 Fetta di insalata + x1 Pane per hamburger › Banco da lavoro  › x6 Hamburger di carne"
    )

    await update.message.reply_text(text, parse_mode="Markdown")


# 👇 QUESTO DEVE STARE FUORI DA TUTTO
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("cucina", cucina))
app.add_handler(CommandHandler("chips", chips))
app.add_handler(CommandHandler("hotdog", hotdog))
app.add_handler(CommandHandler("pasta", pasta))
app.add_handler(CommandHandler("hamburger", hamburger))

app.run_polling()


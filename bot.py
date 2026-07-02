from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8535382395:AAFhvbq-l8uT-BgdI01Z91Sb_1_OeVjQBuo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Il bot funziona 😄")

async def cucina(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍽️ *Ecco a te l'elenco delle ricette da noi possedute!*\n\n"
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
        "Patata > Tagliere > Chips x4\nChips > Friggitrice > Chips Cotte\n\n"
        "» Chips alla paprika:\n"
        "\tChips Cotte + Paprika > Chips alla Paprika x2\n\n"
        "Da usare sul banco da lavoro."
        
    )

async def hotdog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Ecco le ricette degli HotDog:*\n\n"
        "»HotDog Classico:\n"
        "\t x1 Pane per hotdog + x1 Wurstel cotto + x1 Maionese + x1 Ketchup › Banco da Lavoro > x4 Hot dog\n\n"
        "»HotDog Vegano:\n"
        "\tx1 Pane per hotdog + x1 Wurstel veg cotto + x1 Lattuga + x1 Pomodoro › Banco da Lavoro > x4 Hot dog veg\n\n"
        "»HotDog con Cipolla Croccante:\n"
        "\tx1 Pane per hotdog + x1 Wurstel cotto + x1 Cipolle fritte + x1 Senape › Banco da lavoro > HotDog con Cipolla x4\n\n"
        "Il pane per hotdog si ottiene tagliando pane per hamburger su un tagliere con un coltello."
        
    )

    await update.message.reply_text(text, parse_mode="Markdown")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("cucina", cucina))

app.add_handler(CommandHandler("chips", chips))

app.add_handler(CommandHandler("hotdog", hotdog))

app.run_polling()
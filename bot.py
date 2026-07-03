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
        "🍝 *Ecco a te i vari tipi di pasta:*\n\n"
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
        "🍔 *Ecco a te i vari hamburger:*\n\n"
        "» Cheeseburger:\n"
        "x1 Pane per hamburger + x1 Hamburger di manzo + x1 Cheddar + x1 Bacon + x1 Pane per hamburger › Banco da lavoro  › x5 Cheeseburger con bacon\n\n"
        "» Carne:\n"
        "x1 Pane per hamburger + x1 Fetta di pomodoro + x1 Hamburger di manzo + x1 Cheddar + x1 Fetta di insalata + x1 Pane per hamburger › Banco da lavoro  › x6 Hamburger di carne"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def nachos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🧀 *Ecco a te i vari nachos:*\n\n"
        "» Nachos al Formaggio:\n"
        "x1 Nachos + x1 Spezia di jalapeno + x1 Cheddar › x3 Nachos al formaggio\n\n"
        "» Nachos alla Paprika:\n"
        "x1 Nachos + x1 Paprika + x1 Cheddar › Banco da lavoro › x3 Nachos alla paprika"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def wrap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌯 *Ecco a te i nostri wrap:*\n\n"
        "» Cheese Bacon Wrap:\n"
        "x1 Piadina cotta + x1 Bacon cotto + x1 Cheddar + x1 Hamburger di carne spezzettato ›  4 Cheese Bacon Wrap\n\n"
        "⚠️*Nota:* taglia l'hamburger di carne con un coltello sul tagliere per ottenere hamburger di carne spezzettato!\n\n"
        "» Wrap Pesce:\n"
        "x1 Piadina cotta + x1 Salsa tartara + x1 Merluzzo fritto spezzettato › Banco da lavoro > x3 Wrap di pesce\n\n"
        "⚠️*Nota:* taglia il merluzzo fritto con un coltello sul tagliere per ottenere merluzzo fritto spezzettato!"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def uramaki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🥑 *Ecco a te i vari uramaki:*\n\n"
        "» Uramaki al salmone:\n"
        "x1 Salsa di soia + x1 Salsa teriyaki + x1 Sashimi di salmone + x1 Riso bollito + x1 Alga essiccata › Banco da lavoro › x5 Uramaki al salmone\n\n"
        "» Uramaki al tonno:\n"
        "x1 Salsa di soia + x1 Salsa teriyaki + x1 Sashimi di tonno + x1 Riso bollito + x1 Alga essiccata › Banco da lavoro › x5 Uramaki al tonno\n\n"
        "» Uramaki al formaggio:\n"
        "x1 Formaggio spalmabile + x1 Salsa piccante + x1 Cheddar + x1 Riso bollito + x1 Alga essiccata › Banco da lavoro › x5 Uramaki al formaggio\n\n"
        "Per ottenere il *sashimi*, consulta /sashimi!"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def nigiri(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍣 *Ecco a te i vari nigiri:*\n\n"
        "» Nigiri al Polpo:\n"
        "x1 Riso bollito + x1 Sashimi al polpo + Alga essiccata › Banco da lavoro › x3 Nigiri al polpo\n\n"
        "» Nigiri Tropicale:\n"
        "x1 Riso bollito + x1 Sashimi tropicale + x1 Alga essicata  ›  Banco da lavoro  › x3 Nigiri tropicali\n\n"
        "» Nigiri al Salmone:\n"
        "x1 Riso bollito + x1 Sashimi di Salmone + x1 Alga essiccata › Banco da lavoro › x3 Nigiri al salmone\n\n"
        "Per ottenere il *sashimi*, consulta /sashimi!"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def hosomaki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🐟 *Ecco a te i vari hosomaki:*\n\n"
        "» Hosomaki al Salmone:\n"
        "x1 Sashimi al salmone + x1 Riso bollito + Alga essiccata › Banco da lavoro › x3 Hosomaki al salmone\n\n"
        "» Hosomaki al Tonno:\n"
        "x1 Sashimi di tonno + x1 Riso bollito + x1 Alga essiccata › Banco da lavoro › x3 Hosomaki al tonno\n\n"
        "Per ottenere il *sashimi*, consulta /sashimi!"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def sashimi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Per ottenere il *sashimi*, prendi uno dei seguenti:\n\n"
        "» Polpo\n"
        "» Tonno\n"
        "» Salmone\n"
        "» Pesce tropicale\n"
        "» Anguilla\n\n"
        "Metti su un tagliere e taglia con il coltello!"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def tacos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌮 *Ecco a te i vari tacos:*\n\n"
        "» Tacos di Carne:\n"
        "x1 Paprika + x1 Fetta d’insalata + x1 Hamburger di carne spezzettato + x1 Piadina cotta › Banco da lavoro › x4 Tacos di carne\n\n"
        "» Tacos piccante:\n"
        "x1 Spezia Piccante + x1 Fetta d’insalata + x1 Hamburger di carne spezzettato + x1 Piadina cotta › Banco da lavoro › x4 Tacos di carne\n\n"
        "⚠️*Nota:* taglia l'hamburger di carne con un coltello sul tagliere per ottenere hamburger di carne spezzettato!\n\n"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def torta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍰 *Ecco a te le nostre torte:*\n\n"
        "» Torta al cioccolato:\n"
        "x2 Cioccolato fondente + x1 Impasto per dolci › Banco da lavoro › x3 Torta al cioccolato\n\n"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def macaron(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🥯 *Ecco a te tutti i nostri macaron:*\n\n"
        "» Macaron alla Fragola:\n"
        "Fragola > Tagliere (Coltello) > x2 Fetta di Fragola\n\n"
        "x1 Impasto piccolo + x2 Fetta di fragola + x1 Impasto piccolo › Banco da lavoro > x4 Macaron alla Fragola\n\n"
        "» Macaron Cioccolato:\n"
        "x1 Impasto piccolo + x1 Cacao + x1 Impasto piccolo › Banco da lavoro > x3 Macaron al Cioccolato\n\n"
        "» Macaron alla Vaniglia:\n"
        "x1 Impasto piccolo + x1 Vaniglia + x1 Impasto piccolo › Banco da lavoro > x3 Macaron alla Vaniglia\n\n"
        "» Macaron Pistacchio:\n"
        "x1 Impasto piccolo + x1 Pistacchio + x1 Impasto piccolo › Banco da lavoro > x3 Macaron al Pistacchio\n\n"
        "» Macaron ai Frutti di Bosco:\n"
        "x1 Impasto piccolo + x1 Frutti di Bosco + x1 Impasto piccolo › Banco da lavoro > x3 Macaron ai Frutti di Bosco\n\n"
        "» Macaron ai Mirtilli:\n"
        "x1 Impasto piccolo + x1 Mirtilli + x1 Impasto piccolo › Banco da lavoro > x3 Macaron ai Mirtilli\n\n"
        "⚠️*Nota:* per fare l'impasto piccolo, taglia l'impasto per dolci nel tagliere."
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
app.add_handler(CommandHandler("nachos", nachos))
app.add_handler(CommandHandler("wrap", wrap))
app.add_handler(CommandHandler("uramaki", uramaki))
app.add_handler(CommandHandler("nigiri", nigiri))
app.add_handler(CommandHandler("hosomaki", hosomaki))
app.add_handler(CommandHandler("sashimi", sashimi))
app.add_handler(CommandHandler("tacos", tacos))
app.add_handler(CommandHandler("torta", torta))
app.add_handler(CommandHandler("macaron", macaron))


app.run_polling()


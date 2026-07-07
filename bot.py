from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler
import time
import asyncio
import os
import sqlite3

TOKEN = os.getenv("TOKEN")
cooldowns = {}
#-----------------------INIZIO DB PER COLLEZIONE!
# Connessione al database
DB_NAME = "database.db"

conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()

# Tabella utenti
cursor.execute("""
CREATE TABLE IF NOT EXISTS utenti (
    user_id INTEGER PRIMARY KEY,
    ultima_apertura INTEGER
)
""")

# Tabella collezione
cursor.execute("""
CREATE TABLE IF NOT EXISTS collezione (
    user_id INTEGER,
    oggetto TEXT,
    quantita INTEGER,
    PRIMARY KEY (user_id, oggetto)
)
""")

conn.commit()

PACK_ITEMS = [
    {
        "nome": "🥁 Tamburo di SamuGiovyPaoLeo",
        "rarita": "Comune",
        "peso": 30
    },
    {
        "nome": "🌿 Bush di Angelo Bush",
        "rarita": "Non comune",
        "peso": 25
    },
    {
        "nome": "🏝️ Maldive di Loris",
        "rarita": "Non comune",
        "peso": 25
    },
    {
        "nome": "🍵 Matcha di Carla",
        "rarita": "Raro",
        "peso": 10
    },
    {
        "nome": "🪵 Palo in culo di Giorgio",
        "rarita": "Molto raro",
        "peso": 5
    },
    {
        "nome": "🦶 Piedino di Raffy",
        "rarita": "Ultra raro",
        "peso": 3
    },
    {
        "nome": "⚽ Palla destra di Melo",
        "rarita": "Leggendario",
        "peso": 1
    },
    {
        "nome": "⚽ Palla sinistra di Melo",
        "rarita": "Leggendario",
        "peso": 1
    }
]








#-----------------------------------------INIZIO COMANDI BASE

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Il bot funziona 😄")


async def comandi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "*Lista comandi disponibili*:\n\n"
        "» /cucina\n"
        "» /culo\n"
        "» /gioca\n"
        "» /bush\n"
        "» /apri \n"
        "» /collezione"
        "TEST"
    )

    await update.message.reply_text(text)



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
        "» Temaki /temaki\n\n"
        "» Tacos /tacos\n\n"
        "» Anelli di cipolla /anelli\n\n"
        "» Insalate /insalate\n\n"
        "» Cotoletta /cotoletta\n\n"
        "» Tasty Basket e varie di Pollo /pollo\n\n"
        "🍰 *Dolci:*\n\n"
        "» Torta /torta\n\n"
        "» Pancake /pancake\n\n"
        "» Croissant /croissant\n\n"
        "» Fragole /fragole\n\n"
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
        "x1 Pane per hamburger + x1 Fetta di pomodoro + x1 Hamburger di manzo + x1 Cheddar + x1 Fetta di insalata + x1 Pane per hamburger › Banco da lavoro  › x6 Hamburger di carne\n\n"
        "» Vegano:\n"
        "x1 Pane per hamburger + x1 Fetta di pomodoro + x1 Hamburger vegano + x1 Cheddar + x1 Fetta di insalata + x1 Pane per hamburger › Banco da lavoro  › x6 Hamburger vegano\n\n"
        "» Pollo:\n"
        "x1 Pane per hamburger + x1 Fetta di pomodoro + x1 Hamburger di pollo + x1 Cheddar + x1 Fetta di insalata + x1 Pane per hamburger › Banco da lavoro  › x6 Hamburger di pollo\n\n"
        "» Pesce:\n"
        "x1 Pane per hamburger + x1 Salsa tartara + x1 Merluzzo fritto + x1 Pane per hamburger > Banco da Lavoro > x4 Hamburger di pesce\n"
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
        "⚠️*Nota:* taglia il merluzzo fritto con un coltello sul tagliere per ottenere merluzzo fritto spezzettato!\n\n"
        "» Wrap di pollo:\n"
        "x1 Piadina cotta + x1 Fetta di pomodoro + x1 Fetta d’Insalata + x1 Cheddar + x1 Hamburger di Pollo spezzettato › Banco da lavoro › x5 Wrap di Pollo\n\n"
        "⚠️*Nota:* taglia hamburger di pollo con un coltello sul tagliere per ottenere hamburger di pollo spezzettato!\n\n"
        "» Wrap vegano:\n"
        "x1 Piadina cotta + x1 Fetta di pomodoro + x1 Fetta d'insalata + x1 Cheddar + x1 Hamburger vegano spezzettato > Banco da lavoro > x5 Wrap vegano\n\n"
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
        "» Tacos piccante:\n"
        "x1 Spezia piccante + x1 Salsa tartara + x1 Merluzzo fritto spezzettato + x1 Piadina cotta › Banco da lavoro › x4 Tacos di pesce\n\n"
        "⚠️*Nota:* taglia l'hamburger di carne con un coltello sul tagliere per ottenere hamburger di carne spezzettato!\n\n"
        "⚠️*Nota 2:* taglia il merluzzo fritto con un coltello sul tagliere per ottenere merluzzo fritto spezzettato!\n\n"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def anelli(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🧅 *Ecco a te gli anelli di cipolla:*\n\n"
        "x1 Cipolla (tagliata) + x1 Sale (?) + x1 Pastella (?) > Banco da lavoro > x3 Anelli di cipolla\n"
        "Friggere gli anelli di cipolla"
        
    )

    await update.message.reply_text(text, parse_mode="Markdown")



async def insalate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🥗 *Ecco a te le nostre insalate:*\n\n"
        "» Insalata Mista:\n"
        "x1 Papaya + x1 Maionese + x1 Fetta di Pomodoro + x2 Fetta d’insalata > Banco da Lavoro > x5 Insalata mista\n\n"

        
    )

    await update.message.reply_text(text, parse_mode="Markdown")


async def cotoletta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🥩 *Ecco a te le cotolette:*\n\n"
        "• x1 pastella + x1 bistecca › x2 bistecca impanato\n"
        "• x1 lattuga + x1 fetta di pomodoro + x1 bistecca impanato › x3 cotoletta"
        
    )

    await update.message.reply_text(text, parse_mode="Markdown")


async def pollo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🐔 *Ecco a te alcune ricette di pollo:*\n\n"
        "» Alette di Pollo:\n"
        "Pollo › tagliere › 2x coscia pollo\n"
        "Coscia pollo › alette di pollo\n"
        "Aletta + salsa agrodolce + aletta › banco da lavoro › 2x alette crude\n"
        "2x alette crude › forno › 2x Alette di pollo cotte\n\n"
        "» Tasty Basket:\n"
        "•x1 Pollo › Tagliere › x2 Coscia di pollo\n"
        "•x1 Coscia di pollo › Tagliere › x1 Alette di pollo crude\n"
        "•x1 Alette di pollo crude › Tagliere › x1 Nugget crudo\n"
        "•x1 Nugget crudo + x1 Pastella + x1 Nugget crudo › Banco da Lavoro › x2 Nugget impanato\n"
        "•x12 Nugget impanato › Friggitrice › x12 Nugget fritto\n"
        "•x1 Sale + x3 Nugget fritto + x1 Maionese + x1 Ketchup › Banco da Lavoro › x6 Tasty basket\n"

        
    )

    await update.message.reply_text(text, parse_mode="Markdown")



async def temaki(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍙Ecco a te i nostri temaki:\n\n"
        "» Temaki al Tonno:\n"
        "x1 Riso bollito + x1 Alga essiccata + x1 Avocado (fetta) + x1 Sashimi Tonno > Banco da lavoro > x4 Temaki al tonno\n\n"
        "» Temaki al Salmone\n"
        "» x1 Riso bollito + x1 Alga essiccata + x1 (non so cosa sia, 3 filini gialli) + x1 Sashimi Tonno > Banco da lavoro > x4 Temaki al tonno\n\n"
        "Per ottenere il *sashimi*, consulta /sashimi!"
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def torta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍰 *Ecco a te le nostre torte:*\n\n"
        "» Torta al cioccolato:\n"
        "x2 Cioccolato fondente + x1 Impasto per dolci › Banco da lavoro › x3 Torta al cioccolato\n\n"
        "» Torta Saker:\n"
        "x2 Cioccolato fondente + x1 Arancia + x1 Impasto per dolci › Banco da lavoro › x4 Saker\n\n"
        "» Cheesecake:\n"
        "x2 Fetta di fragola + x1 Formaggio spalmabile + x1 Impasto per dolci › Banco da lavoro › x4 Cheesecake\n"
        "Le fette di fragola si ottengono tagliando fragola su tagliere.\n\n"
    )

    await update.message.reply_text(text, parse_mode="Markdown")



async def pancake(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🥞 *Ecco a te i pancake:*\n\n"
        "» Pancake generico:\n"
        "x2 Impasto per dolci > Padella > x2 Pancake\n\n"
        "» Pancake al caramello:\n"
        "x1 Pancake + x1 Caramello + x1 Burro › Banco da lavoro › x3 Pancake al caramello\n\n"
        "» Pancake al pistacchio:\n"
        "x1 Pancake + x1 Pistacchio + x1 Panna (credo) › Banco da lavoro › x3 Pancake al pistacchio\n\n"
        "» Pancake al cioccolato:\n"
        "x1 Pancake + x1 Fragola + x1 Cioccolato Sciolto + x1 Panna (credo) › Banco da lavoro › x4 Pancake al cioccolato\n"
        "Il cioccolato sciolto si ottiene mettendo cioccolato fondente in una pentola con acqua."
    )

    await update.message.reply_text(text, parse_mode="Markdown")

async def croissant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🥐 *Ecco a te i croissant:*\n\n"
        "» Croissant:\n"
        "x1 Impasto per dolci › Tagliere › x2 Impasto piccolo per dolci\n"
        "x4 Impasto piccolo per dolci > Banco da lavoro > x2 Croissant crudo\n"
        "x4 Croissant crudo > Forno > x4 Croissant\n\n"

    )

    await update.message.reply_text(text, parse_mode="Markdown")


async def fragole(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🍓 *Ecco a te le fragole:*\n\n"
        "» Fragole con panna:\n"
        "x1 Fragola + x1 Panna › Banco da Lavoro › x3 Fragola con panna\n\n"
        "» Fragole al cioccolato:\n"
        "x3 Cacao (forse) > Pentola > x3 Cioccolato\n"
        "x1 Fragola + x1 Cioccolato > Banco da Lavoro > x3 Fragola al cioccolato\n"

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

async def culo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "CULO"
    )

    await update.message.reply_text(text, parse_mode="Markdown")


async def gioca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎁 Apri il pacco", callback_data="gioco")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎲 Premi il pulsante per tentare la fortuna!",
        reply_markup=reply_markup
    )

async def bottone_gioco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    await query.answer()

    # 🧊 COOLDOWN 10 MINUTI
    now = time.time()

    if user_id in cooldowns:
        last_time = cooldowns[user_id]
        if now - last_time < 600:
            remaining = int(600 - (now - last_time))
            minutes = remaining // 60
            seconds = remaining % 60

            await query.edit_message_text(
                f"⏳ Aspetta prima di giocare di nuovo!\n"
                f"Riprova tra {minutes}m {seconds}s"
            )
            return

    cooldowns[user_id] = now

    # 🎰 ANIMAZIONE SLOT
    slot_frames = [
        "🎰 | 🍒 | 🍋 | 🔔",
        "🎰 | 🍋 | 🔔 | 🍒",
        "🎰 | 🔔 | 🍒 | 🍋",
        "🎰 | 🍒 | 🍒 | 🍒",
    ]

    msg = await query.edit_message_text("🎰 Girando la slot...")

    for frame in slot_frames:
        await asyncio.sleep(0.7)
        await msg.edit_text(f"🎰 SLOT MACHINE\n\n{frame}")

    # 🎲 RISULTATO FINALE (CASINO SYSTEM)
    roll = random.randint(1, 100)

    if roll <= 50:
        await msg.edit_text(
        "🎰 RISULTATO FINALE\n\n"
        "😢 Non hai vinto questa volta.\n\n"
        "⏳ Riprova tra 10 minuti!"
        )
        return

    elif roll <= 80:
        premio = "🌿 1 bush"
        rarita = "Comune"

    elif roll <= 92:
        premio = "🍱 1 stack di cibo fvesco"
        rarita = "Non comune"

    elif roll <= 98:
        premio = "👑 1 ingresso della manager sul server"
        rarita = "Raro"

    else:
        premio = "🎟 1 fiches (offerta da Fvostolo)"
        rarita = "Leggendario 💎"

    await msg.edit_text(
        f"🎰 RISULTATO FINALE\n\n"
        f"🎉 Hai vinto!\n\n"
        f"🏆 Premio: {premio}\n"
        f"📊 Rarità: {rarita}\n\n"
        f"⏳ Potrai giocare di nuovo tra 10 minuti."
    )


async def bush(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "<b>Bush?!</b>\n\n"
        '<a href="https://www.instagram.com/angelo_busc?utm_source=ig_web_button_share_sheet&utm_medium=copy_link">bush</a>'
    )

    await update.message.reply_text(text, parse_mode="HTML")

async def apri(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    now = int(time.time())

    # Controlla se l'utente esiste
    cursor.execute(
        "SELECT ultima_apertura FROM utenti WHERE user_id = ?",
        (user_id,)
    )
    result = cursor.fetchone()

    # Se è il primo utilizzo
    if result is None:
        cursor.execute(
            "INSERT INTO utenti (user_id, ultima_apertura) VALUES (?, ?)",
            (user_id, 0)
        )
        conn.commit()
        ultima_apertura = 0
    else:
        ultima_apertura = result[0]

    # Cooldown di 12 ore
    cooldown = 12 * 60 * 60

    if now - ultima_apertura < cooldown:
        restante = cooldown - (now - ultima_apertura)

        ore = restante // 3600
        minuti = (restante % 3600) // 60

        await update.message.reply_text(
            f"Hai già aperto un pacchetto.\n"
            f"Potrai aprirne un altro tra {ore}h {minuti}m."
        )
        return

    # Estrazione casuale
    oggetto = random.choices(
        PACK_ITEMS,
        weights=[item["peso"] for item in PACK_ITEMS],
        k=1
    )[0]

    # Aggiorna cooldown
    cursor.execute(
        "UPDATE utenti SET ultima_apertura = ? WHERE user_id = ?",
        (now, user_id)
    )

    # Controlla se l'oggetto esiste già
    cursor.execute(
        """
        SELECT quantita
        FROM collezione
        WHERE user_id = ? AND oggetto = ?
        """,
        (user_id, oggetto["nome"])
    )

    trovato = cursor.fetchone()

    if trovato:
        cursor.execute(
            """
            UPDATE collezione
            SET quantita = quantita + 1
            WHERE user_id = ? AND oggetto = ?
            """,
            (user_id, oggetto["nome"])
        )
    else:
        cursor.execute(
            """
            INSERT INTO collezione(user_id, oggetto, quantita)
            VALUES (?, ?, 1)
            """,
            (user_id, oggetto["nome"])
        )

    conn.commit()

    await update.message.reply_text(
        f"📦 Hai aperto il tuo pacchetto!\n\n"
        f"Hai ottenuto:\n\n"
        f"{oggetto['nome']}\n\n"
        f"Rarità: {oggetto['rarita']}"
    )



async def collezione(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    cursor.execute("""
        SELECT oggetto, quantita
        FROM collezione
        WHERE user_id = ?
        ORDER BY quantita DESC
    """, (user_id,))

    risultati = cursor.fetchall()

    if not risultati:
        await update.message.reply_text(
            "La tua collezione è vuota.\n\nApri un pacchetto con /apri!"
        )
        return

    totale_oggetti = sum(qta for _, qta in risultati)
    oggetti_unici = len(risultati)

    testo = "═══════ COLLEZIONE ═══════\n\n"

    for oggetto, quantita in risultati:
        testo += f"{oggetto} ×{quantita}\n"

    testo += "\n────────────────────\n\n"
    testo += f"Oggetti unici: {oggetti_unici}/{len(PACK_ITEMS)}\n"
    testo += f"Totale oggetti: {totale_oggetti}"

    await update.message.reply_text(testo)

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
app.add_handler(CommandHandler("temaki", temaki))
app.add_handler(CommandHandler("anelli", anelli))
app.add_handler(CommandHandler("insalate", insalate))
app.add_handler(CommandHandler("pollo", pollo))
app.add_handler(CommandHandler("cotoletta", cotoletta))
app.add_handler(CommandHandler("torta", torta))
app.add_handler(CommandHandler("pancake", pancake))
app.add_handler(CommandHandler("croissant", croissant))
app.add_handler(CommandHandler("fragole", fragole))
app.add_handler(CommandHandler("macaron", macaron))
app.add_handler(CommandHandler("culo", culo))
app.add_handler(CommandHandler("gioca", gioca))
app.add_handler(CallbackQueryHandler(bottone_gioco))
app.add_handler(CommandHandler("comandi", comandi))
app.add_handler(CommandHandler("bush", bush))
app.add_handler(CommandHandler("apri", apri))
app.add_handler(CommandHandler("collezione", collezione))


app.run_polling()


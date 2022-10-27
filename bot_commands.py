from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
async    def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name} -  вах  генацвали!')

async    def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async    def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help\n/sum\n/diff\n/mult\n/del\n')

async    def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # sum 123 534543
    x = float(items[1])
    y = float(items[2])

    await update.message.reply_text(f'{x}+{y} = {x+y}')

async    def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # mult 123 534543
    a = float(items[1])
    b = float(items[2])

    await update.message.reply_text(f'{a}*{b} = {a*b}')

async    def diff_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # diff 123 534543
    a = float(items[1])
    b = float(items[2])

    await update.message.reply_text(f'{a}-{b} = {a-b}')

async    def del_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # del 123 534543
    a = float(items[1])
    b = float(items[2])

    await update.message.reply_text(f'{a}/{b} = {a/b}')
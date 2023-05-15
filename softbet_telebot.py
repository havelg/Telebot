from typing import Final
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN: Final = '5838924537:AAFn-DUwbMAR3_t2YJ1-oB3c2XVnQCWCBKQ'
BOT_USERNAME: Final = '@your_bot_user'


def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if 'about' in processed:
        return 'Welcome to SOFTBET.\n\nThe best Telegram channel with football tips and analysis!\nThe leading pathway to wealth 💪.\n💰95% accurate on 3 free tips daily\nAccurate longshot everyweekend\nThere is also a paid VIP group where a game of 2 odds is posted daily.\n\nUse the menu button to send a command to this bot'
        
    if 'joinchannel' in processed:
        return 'NOTE BET IS A GAME OF RISK ❗️❗️SOFTBET IS NOT RESPONSIBLY FOR ANY LOSS NO REFUND ON ANY SUBSCRIPTION PAYMENT 🔞🔞\n\n Join our channel at https://t.me/softbetz\n\nGet the latest news about our games, winnings and updates'

    if 'vip' in processed:
        return 'Thanks for choosing our SOFTBET subscription.\nVIP access is available for premium members only.\n\nVIP Subscription Fee NGN 18,000\nDuration 1 month.\n\nSOFTBET ACCOUNT DETAILS\nBANK NAME: Kuda Bank\nACCOUNT NUMBER: 2010362008\nACCOUNT NAME: Havel Godwin\n\nDrop screenshots for confirmation of your payment.'

    if 'admin' in processed:
        return 'To contact the admin, t.me/SOFTBET001.'

    if 'notice' in processed:
        return 'Important notice: Tomorrow\'s meeting has been rescheduled to 3 PM.'

    return 'Kindly use the menu button to send a command to this bot.'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    response: str = handle_response(text)

    # Reply with the response
    print('Bot:', response)
    await update.message.reply_text(response)


# Log errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Message handler for all incoming messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)

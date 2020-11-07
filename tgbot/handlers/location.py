import telegram

from tgbot.models import User, Location


def ask_for_location(update, context):
    u = User.get_user(update, context)

    context.bot.send_message(
        chat_id=u.user_id, text="Would you mind sharing your location?",
        reply_markup=telegram.ReplyKeyboardMarkup([
            [telegram.KeyboardButton(text="Send 🌏🌎🌍", request_location=True)]
        ]),
    )


def location_handler(update, context):
    u = User.get_user(update, context)
    lat, lon = update.message.location.latitude, update.message.location.longitude
    l = Location.objects.create(user=u, latitude=lat, longitude=lon)

    update.message.reply_text(
        f"Thanks for 🌏🌎🌍",
        reply_markup=telegram.ReplyKeyboardRemove(),
    )    

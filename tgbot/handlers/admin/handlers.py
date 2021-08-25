import datetime

import telegram
from django.utils.timezone import now

from tgbot.handlers.admin import static_text
from tgbot.models import User


def admin(update, context):
    """ Show help info about all secret admins commands """
    u = User.get_user(update, context)
    if not u.is_admin:
        return

    return update.message.reply_text(static_text.secret_admin_commands)


def stats(update, context):
    """ Show help info about all secret admins commands """
    u = User.get_user(update, context)
    if not u.is_admin:
        return

    text = static_text.users_amount_stat.format(
        user_count=User.objects.count(),  # this may be ineffective if there are a lot of users.
        active_24=User.objects.filter(updated_at__gte=now() - datetime.timedelta(hours=24)).count()
    )

    return update.message.reply_text(
        text,
        parse_mode=telegram.ParseMode.MARKDOWN,
        disable_web_page_preview=True,
    )

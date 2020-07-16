from django.conf import settings
from django.db.models.signals import post_save

from .handlers import SocketHandler, WebhookHandler
from userdata.models import ServerUtils, Rules

webhook = WebhookHandler(settings.WEBHOOK_ID,
                         settings.WEBHOOK_SECRET)
bot_socket = SocketHandler(settings.BOT_SOCKET_IP,
                           int(settings.BOT_SOCKET_PORT),
                           settings.BOT_SOCKET_TOKEN)


def reload_rules(sender, **kwargs):
    bot_socket.signal("rules")


def reload_serverutils(sender, **kwargs):
    bot_socket.signal("server_meta")


post_save.connect(reload_rules, sender=Rules, dispatch_uid="news")
post_save.connect(reload_serverutils, sender=ServerUtils, dispatch_uid="server")
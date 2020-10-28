from django.contrib.auth.models import User as AuthUser
from userdata.models import Admins, Guild


def get_admin_guild_list(guilds):
    tortoise_guilds = Guild.get_id_list()
    return [
        guild["id"] for guild in guilds if int(guild["permissions"]) & 8 and int(guild["id"]) in tortoise_guilds
    ]


def update_guilds(instance: Admins, guild_list: list):
    if instance.guild is not None:
        instance.guild.clear()
    instance.guild.add(*guild_list)
    instance.save()


def create_admin(user_json: dict, admin_guilds: list, password: str):
    auth_user = AuthUser.objects.create_user(username=user_json["id"],
                                             password=password,
                                             is_staff=True,
                                             first_name=user_json["username"],
                                             email=user_json["email"]
                                             )
    admin_user = Admins.objects.create(authuser=auth_user, user_id=user_json["id"])
    update_guilds(admin_user, admin_guilds)
    return auth_user
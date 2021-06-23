import discord
import asyncio
import random
from oauth2client import file as oauth_file, client, tools
from discord.ext import commands, tasks

################ Channel, Server, and User IDs ###########################
sphinx_id = 108381986166431744
sk_server = 401186250335322113
bk_server = 691130488483741756
c_server = 800129405350707200
servers = [sk_server, bk_server, c_server]

sk_bot = 401212001239564288
bk_bot = 691205255664500757
bk_ann = 695801936095740024 #BK #announcement
c_bot = 800129405350707200
botinit_id = [sk_bot, bk_bot, c_bot]


class Bsb(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(ctx):
        await ctx.channel.send(f"{client.latency}")


def setup(client):
    client.add_cog(Bsb(client))

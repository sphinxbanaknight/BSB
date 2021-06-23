import discord
import random
import os
import json
import gspread
import pprint
from oauth2client import file as oauth_file, client, tools
from apiclient.discovery import build
from httplib2 import Http
import time
import datetime
import pytz
import asyncio

from pytz import timezone
from datetime import datetime, timedelta

from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands, tasks

################ Channel, Server, and User IDs ###########################
sphinx_id = 108381986166431744
ardi_id = 248681868193562624
kriss_id = 694307907835134022
ken_id = 158345623509139456
jude_id = 693741143313088552
cell_id = 192286855025262592
glock_id = 706842108832776223
# servers = [401186250335322113, 691130488483741756, 800129405350707200]
sk_server = 401186250335322113
bk_server = 691130488483741756
c_server = 800129405350707200
servers = [sk_server, bk_server, c_server]

sk_bot = 401212001239564288
bk_bot = 691205255664500757
bk_ann = 695801936095740024  # BK #announcement
c_bot = 800129405350707200
botinit_id = [sk_bot, bk_bot, c_bot]
authorized_id = [sphinx_id, ardi_id, kriss_id, ken_id, jude_id, cell_id, glock_id]
dev_id = [sphinx_id]

prefix = ["/"]
description = "A bot for sheet+discord linking/automation."
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, description=description, intents=intents)

client.remove_command('help')

@client.event
async def on_ready():
    global isarchived
    global isreminded1
    global isreminded2
    global tf_archive
    global tf_remind1
    global tf_remind2
    global tf_reset
    # global cresence

    for server in client.guilds:
        if server.id == sk_server:
            sphinx = server
            break

    for server in client.guilds:
        if server.id == c_server:
            cresence = server
            break
    #    elif server.id == bk_server:
    #        burger = server

    for channel in sphinx.channels:
        if channel.id == sk_bot:
            botinitsk = channel
            break
    # for channel in burger.channels:
    #    if channel.id == bk_bot:
    #        botinitbk = channel
    #    elif channel.id == bk_ann:
    #        botinitbkann = channel

    print('Bot is online.')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Getting scolded by Ardi'))


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog: {extension}.py loaded')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog: {extension}.py unloaded')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog: {extension}.py reloaded')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')


client.run(os.environ['token'], reconnect=True)